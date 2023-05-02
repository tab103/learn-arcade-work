import random
import arcade
from pyglet.math import Vec2
import math

SPRITE_SCALING_BOX = 3.75
SPRITE_SCALING_PLAYER = 0.085
PLAYER_HEALTH = 100
SPRITE_SCALING_ZOMBIE = .5
TEXTURE_PLAYER_LEFT = 0
TEXTURE_PLAYER_RIGHT = 1
SPRITE_SCALING_AMMO_CRATE = .75
SPRITE_SCALING_HEALTH = 1
SPRITE_SCALING_LASER = .5
AMMO_CRATE_COUNT = 8
ZOMBIE_COUNT = 75
HEALTH_KIT_COUNT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "2D Platform Scroller"
VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1
VIEWPOINT_MARGIN = 300
ZOMBIE_MOVEMENT_SPEED = .375
PLAYER_MOVEMENT_SPEED = 1.025
BULLET_SPEED = 4.5

class Bullet(arcade.Sprite):
    def __init__(self, fname, scale):
        super().__init__(fname, scale)
        self.x_delta = 0
        self.y_delta = 0
        self.life_x = 0
        self.life_y = 0

    def update(self):
        self.center_x += self.x_delta
        self.center_y += self.y_delta
        self.life_x += self.x_delta
        self.life_y += self.y_delta

        # limit bullet life
        if self.life_x > SCREEN_WIDTH or self.life_y > SCREEN_HEIGHT:
            self.remove_from_sprite_lists() # if off screen remove


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING_PLAYER
        self.textures = []
        texture = arcade.load_texture("mafia-7573318_640.png")
        self.textures.append(texture)
        texture = arcade.load_texture("mafia-7573318_640.png",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_PLAYER_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_PLAYER_RIGHT]


class Zombie(arcade.Sprite):
    def follow_sprite(self, player_sprite):

        if self.center_y < player_sprite.center_y:
            self.center_y += min(ZOMBIE_MOVEMENT_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(ZOMBIE_MOVEMENT_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(ZOMBIE_MOVEMENT_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(ZOMBIE_MOVEMENT_SPEED, self.center_x - player_sprite.center_x)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = Player()
        self.zombie_list = Zombie()
        self.wall_list = None
        self.ammo_crate_list = None
        self.bullet_list = None
        self.health_kit_list = None

        # player
        self.player_sprite = Player()

        # Set score
        self.health = 100
        self.ammo = 30

        # Physics engine
        self.physics_engine = None

        # keypress
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.UP_pressed = False
        self.DOWN_pressed = False
        self.LEFT_pressed = False
        self.RIGHT_pressed = False

        # camera
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # sounds from kenney.nl
        self.player_hurt = arcade.load_sound("sfx_lose.ogg")
        self.health_regen = arcade.load_sound("sfx_shieldUp.ogg")

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.ammo_crate_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.health_kit_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 0
        self.player_list.append(self.player_sprite)

        # tile from kenny.nl
        for x in range(200, 1600, 365):
            for y in range(200, 1600, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(8) > 0:
                    wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for y in range(200, 1600, 365):
            for x in range(200, 1600, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(3) > 0:
                    wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for y in range(0, 1800, 64):
            for x in range(0, 1800, 64):
                wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = 0
                self.wall_list.append(wall)

                wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = 1800
                self.wall_list.append(wall)

                wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                wall.center_x = 0
                wall.center_y = y
                self.wall_list.append(wall)

                wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                wall.center_x = 1800
                wall.center_y = y
                self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Create the ammo
        for a in range(AMMO_CRATE_COUNT):

            # Create the ammo_crate instance
            # ammo_crate image from kenney.nl
            ammo_crate = arcade.Sprite("powerupRed_shield.png", SPRITE_SCALING_AMMO_CRATE)

            ammo_crate_placed_successfully = False

            while not ammo_crate_placed_successfully:
                # Position the ammo_crate
                ammo_crate.center_x = random.randrange(200, 1650)
                ammo_crate.center_y = random.randrange(0, 1600)

                # check for collision with wall
                wall_hit_list = arcade.check_for_collision_with_list(ammo_crate, self.wall_list)

                # check for collision with other crates
                ammo_crate_hit_list = arcade.check_for_collision_with_list(ammo_crate, self.ammo_crate_list)

                if len(wall_hit_list) == 0 and len(ammo_crate_hit_list) == 0:
                    ammo_crate_placed_successfully = True

            # Add the ammo_crate to the lists
            self.ammo_crate_list.append(ammo_crate)

        # Create the health kits
        for h in range(HEALTH_KIT_COUNT):

            # Create the kits
            # pill image from kenney.nl
            health_kit = arcade.Sprite("pill_red.png", SPRITE_SCALING_HEALTH)

            health_kit_placed_successfully = False

            while not health_kit_placed_successfully:
                # Position the health_kit
                health_kit.center_x = random.randrange(200, 1650)
                health_kit.center_y = random.randrange(0, 1600)

                # check for collision with wall
                wall_hit_list = arcade.check_for_collision_with_list(health_kit, self.wall_list)

                # check for collision with other kits
                health_kit_hit_list = arcade.check_for_collision_with_list(health_kit, self.health_kit_list)

                if len(wall_hit_list) == 0 and len(health_kit_hit_list) == 0:
                    health_kit_placed_successfully = True

            # Add the health_kit to the lists
            self.health_kit_list.append(health_kit)

        # Create the zombies
        # zombie image from kenney.nl
        for z in range(ZOMBIE_COUNT):

            zombie = Zombie("character_zombie_show.png", SPRITE_SCALING_ZOMBIE)

            zombie_placed_successfully = False

            while not zombie_placed_successfully:
                zombie.center_x = random.randrange(200, 1650)
                zombie.center_y = random.randrange(0, 1600)

                wall_hit_list = arcade.check_for_collision_with_list(zombie, self.wall_list)

                zombie_hit_list = arcade.check_for_collision_with_list(zombie, self.ammo_crate_list)

                if len(wall_hit_list) == 0 and len(zombie_hit_list) == 0:
                    zombie_placed_successfully = True

            self.zombie_list.append(zombie)

        arcade.set_background_color(arcade.color.PASTEL_ORANGE)

    def on_draw(self):
        self.clear()

        # Select the camera
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.ammo_crate_list.draw()
        self.health_kit_list.draw()
        self.bullet_list.draw()
        #self.zombie_list.draw()

        # Select the camera for GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        output1 = "Health: " + str(self.health)
        output2 = "Ammo remaining: " + str(self.ammo)

        arcade.draw_text(output1, 10, 10, arcade.color.BLACK_BEAN, 20)
        arcade.draw_text(output2, 200, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.w_pressed = True
        elif key == arcade.key.S:
            self.s_pressed = True
        elif key == arcade.key.A:
            self.a_pressed = True
        elif key == arcade.key.D:
            self.d_pressed = True
        elif key == arcade.key.UP:
            self.UP_pressed = True
        elif key == arcade.key.DOWN:
            self.DOWN_pressed = True
        elif key == arcade.key.LEFT:
            self.LEFT_pressed = True
        elif key == arcade.key.RIGHT:
            self.RIGHT_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W:
            self.w_pressed = False
        elif key == arcade.key.S:
            self.s_pressed = False
        elif key == arcade.key.A:
            self.a_pressed = False
        elif key == arcade.key.D:
            self.d_pressed = False
        elif key == arcade.key.UP:
            self.UP_pressed = False
        elif key == arcade.key.DOWN:
            self.DOWN_pressed = False
        elif key == arcade.key.LEFT:
            self.LEFT_pressed = False
        elif key == arcade.key.RIGHT:
            self.RIGHT_pressed = False

    def on_mouse_press(self, x, y, button, modifiers):
        print(x % SCREEN_WIDTH, self.player_sprite.center_x % SCREEN_WIDTH - self.view_left, y % SCREEN_HEIGHT, self.player_sprite.center_y % SCREEN_HEIGHT - self.view_bottom)
        if self.ammo > 0:
            y_delta = y - self.player_sprite.center_y
            x_delta = x - self.player_sprite.center_x
            angle = math.atan2(y_delta, x_delta)
            # tan gives first two quadrants, compensate for 3 and 4
            # if rise < 0 and run < 0:
            #     angle = angle + 180
            # elif rise < 0 and run > 0:
            #     angle = angle - 90
            bullet = Bullet("laserRed01.png", SPRITE_SCALING_LASER)
            bullet.angle = math.degrees(angle)
            bullet.x_delta = BULLET_SPEED * math.cos(angle)
            bullet.y_delta = BULLET_SPEED * math.sin(angle)
            bullet.angle = angle - 90
            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.center_y
            self.bullet_list.append(bullet)
            self.ammo -= 1

    def on_update(self, delta_time):

        # Call update on all sprites
        self.physics_engine.update()
        self.bullet_list.update()
        self.ammo_crate_list.update()
        self.health_kit_list.update()
        self.zombie_list.update()
        self.player_list.update()
        #self.bullet_list.update()

        #if self.health <= 0:
        #    arcade.exit()

        # Calculate speed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.w_pressed and not self.s_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.a_pressed and not self.d_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.d_pressed and not self.a_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        # if self.UP_pressed and not self.DOWN_pressed and self.ammo >= 1:
        #     bullet = arcade.Sprite("laserRed01.png", SPRITE_SCALING_LASER)
        #     bullet.angle = 0
        #     bullet.change_y = BULLET_SPEED
        #     bullet.center_x = self.player_sprite.center_x
        #     #bullet.top = self.player_sprite.top
        #     bullet.center_y = self.player_sprite.center_y
        #     self.bullet_list.append(bullet)
        #     self.ammo -= 1
        # elif self.DOWN_pressed and not self.UP_pressed and self.ammo >= 1:
        #     bullet = arcade.Sprite("laserRed01.png", SPRITE_SCALING_LASER)
        #     bullet.angle = 180
        #     bullet.change_y = -BULLET_SPEED
        #     bullet.center_x = self.player_sprite.center_x
        #     #bullet.top = self.player_sprite.top
        #     self.bullet_list.append(bullet)
        #     self.ammo -= 1
        # if self.LEFT_pressed and not self.RIGHT_pressed and self.ammo >= 1:
        #     bullet = arcade.Sprite("laserRed01.png", SPRITE_SCALING_LASER)
        #     bullet.angle = 90
        #     bullet.change_x = -BULLET_SPEED
        #     bullet.center_x = self.player_sprite.center_x
        #     #bullet.top = self.player_sprite.top
        #     self.bullet_list.append(bullet)
        #     self.ammo -= 1
        # elif self.RIGHT_pressed and not self.LEFT_pressed and self.ammo >= 1:
        #     bullet = arcade.Sprite("laserRed01.png", SPRITE_SCALING_LASER)
        #     bullet.angle = 270
        #     bullet.change_x = BULLET_SPEED
        #     bullet.center_x = self.player_sprite.center_x
        #     bullet.top = self.player_sprite.top
        #     self.bullet_list.append(bullet)
        #     self.ammo -= 1

        # list of all sprites that collide with the player.
        health_kit_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.health_kit_list)
        for health_kit in health_kit_hit_list:
            health_kit.remove_from_sprite_lists()
            arcade.play_sound(self.health_regen)
            self.health += 10

        ammo_crate_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.ammo_crate_list)
        for ammo_crate in ammo_crate_hit_list:
            ammo_crate.remove_from_sprite_lists()
            arcade.play_sound(self.health_regen)
            self.ammo += 30

        zombie_hit_list1 = arcade.check_for_collision_with_list(self.player_sprite, self.zombie_list)
        for zombie in zombie_hit_list1:
            zombie.remove_from_sprite_lists()
            arcade.play_sound(self.player_hurt)
            self.health -= 15

        for zombie in self.zombie_list:
            zombie.follow_sprite(self.player_sprite)

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit
            hit_list1 = arcade.check_for_collision_with_list(bullet, self.zombie_list)
            hit_list2 = arcade.check_for_collision_with_list(bullet, self.wall_list)

            # If it did, get rid of the bullet
            if len(hit_list1) > 0:
                bullet.remove_from_sprite_lists()

            if len(hit_list2) > 0:
                bullet.remove_from_sprite_lists()

            # For every zombie we hit, remove
            for zombie in hit_list1:
                zombie.remove_from_sprite_lists()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)



        if changed:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Scroll the screen
        self.scroll_to_player()

    def scroll_to_player(self):
        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
