""" lAB 8 Starter - Modified Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPACE_SHIP_SCALE = 0.08
ROCK_SCALING = 0.1
PANDA_SCALING = 0.05
ROCK_COUNT = 50
PANDA_COUNT = 25

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# inherit from Sprite to add special behavior
class RockSprite(arcade.Sprite):
    def __init__(self, fname, scale):
        super().__init__(fname, scale)
        self.speed = random.randrange(2,5)
        self.rotation_speed = random.randrange(-2, 2)

    def update(self):
        self.center_x += self.speed
        self.center_y += self.speed
        self.angle += self.rotation_speed

# game class inherits from Window
class MyGame(arcade.Window):
    """ Our custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.ship_list = None
        self.panda_list = None
        self.rock_list = None

        # Set up the player info
        self.ship_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds
        self.thrust_sound = arcade.load_sound("thrust.wav", False)
        self.collision_sound = arcade.load_sound('collision.wav', False)
        self.pickup_sound = arcade.load_sound('pickup.wav', False)
        self.pickup_player = None
        self.collision_player = None
        self.thrust_player = None

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.ship_list = arcade.SpriteList()
        self.panda_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.ship_sprite = arcade.Sprite("spaceship.png", SPACE_SHIP_SCALE)
        self.ship_sprite.center_x = SCREEN_WIDTH / 2
        self.ship_sprite.center_y = SCREEN_HEIGHT / 2
        self.ship_list.append(self.ship_sprite)
        self.ship_sprite.textures.append(arcade.load_texture("spaceship.png", flipped_horizontally=True))
        self.ship_sprite.textures.append(arcade.load_texture("spaceship.png"))

        self.ship_xspeed = 0
        self.ship_yspeed = 0
        self.SPEED_MAX = 3
        self.DRIFT_SPEED = 0.1
        self.xidle = True

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        # Create rocks
        for i in range(ROCK_COUNT):

            rock = RockSprite("rock.png", ROCK_SCALING)

            # Position the rock, each will have a random speed
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.rock_list.append(rock)

        # Create pandas
        for i in range(PANDA_COUNT):

            panda = arcade.Sprite("space_panda.png", PANDA_SCALING)

            # Position the coin
            panda.center_x = random.randrange(SCREEN_WIDTH)
            panda.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.panda_list.append(panda)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.panda_list.draw()
        self.ship_list.draw()
        self.rock_list.draw()

        # Put the text on the screen.
        output = f"Panda's Rescued: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """ Movement and game logic """
        if self.xidle:
            self.ship_xspeed += self.DRIFT_SPEED
            if self.ship_xspeed >= 0:
                self.ship_xspeed = 0

        # up/down
        if self.up:
            self.ship_yspeed += 2
        elif self.down:
            self.ship_yspeed -= 2

        # left/right
        if self.left:
            self.ship_xspeed -= 2
        elif self.right:
            self.ship_xspeed += 2

        # if neither up or down, stop
        if not (self.down or self.up):
            self.ship_yspeed = 0

        # change ship image dependign on direction
        if self.ship_xspeed > 0 and self.ship_sprite.texture is not self.ship_sprite.textures[0]:
            self.ship_sprite.texture = self.ship_sprite.textures[0]
        elif self.ship_xspeed <= 0 and self.ship_sprite.texture is not self.ship_sprite.textures[1]:
            self.ship_sprite.texture = self.ship_sprite.textures[1]

        # regulate horizontal speed
        if self.ship_xspeed > self.SPEED_MAX:
            self.ship_xspeed = self.SPEED_MAX
        if self.ship_xspeed < -self.SPEED_MAX:
            self.ship_xspeed = -self.SPEED_MAX

        # regulate vertical speed
        if self.ship_yspeed > self.SPEED_MAX:
            self.ship_yspeed = self.SPEED_MAX
        if self.ship_yspeed < -self.SPEED_MAX:
            self.ship_yspeed = -self.SPEED_MAX

        # update in x off-screen condition
        if self.ship_sprite.center_x < 0:
            self.ship_sprite.center_x = SCREEN_WIDTH
        if self.ship_sprite.center_x > SCREEN_WIDTH:
            self.ship_sprite.center_x = 0

        # update in y off-screen condition
        if self.ship_sprite.center_y < 0:
            self.ship_sprite.center_y = SCREEN_HEIGHT
        if self.ship_sprite.center_y > SCREEN_HEIGHT:
            self.ship_sprite.center_y = 0

        # update ship position
        self.ship_sprite.center_x += self.ship_xspeed
        self.ship_sprite.center_y += self.ship_yspeed

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.panda_list.update()
        self.rock_list.update()

        # check for asteroids hitting asteroids
        collide_list = []
        for rock in self.rock_list:
            hit_list = arcade.check_for_collision_with_list(rock,
                            self.rock_list)
            if hit_list:
                collide_list.append(rock)

        for rock in collide_list:
            rock.speed = rock.speed = -rock.speed
            rock.rotation_speed = -rock.rotation_speed

        recreate_count = 0
        for rock in self.rock_list:
            if rock.center_x > SCREEN_WIDTH:
                rock.remove_from_sprite_lists()
                recreate_count += 1

        # recreate the lost rocks
        for i in range(recreate_count):
            rock = RockSprite("rock.png", ROCK_SCALING)

            # Position the rock somewhere on the left edge
            rock.center_x = 0
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the rock to the lists
            self.rock_list.append(rock)

        # Generate a list of panda's picked up
        hit_list = arcade.check_for_collision_with_list(self.ship_sprite,
                                                        self.panda_list)
        # Remove pandas from the list and increment score
        for panda in hit_list:
            panda.remove_from_sprite_lists()
            self.score += 1
            if not self.pickup_player or not self.pickup_player.playing:
                self.pick_player = arcade.play_sound(self.pickup_sound)

        hit_list = arcade.check_for_collision_with_list(self.ship_sprite,
                                                        self.rock_list)

        # For each collided rock, remove from the list and decrement score
        for rock in hit_list:
            rock.remove_from_sprite_lists()
            self.score -= 1
            if not self.collision_player or not self.collision_player.playing:
                self.collision_player = arcade.play_sound(self.collision_sound)

        # bread crumb technique
        print(self.ship_xspeed, self.xidle)

    # Configure Key Handling Events
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            if not self.thrust_player or not self.thrust_player.playing:
                self.thrust_player = arcade.play_sound(self.thrust_sound)
            self.left = True
            self.right = False
            self.xidle = False
        elif key == arcade.key.RIGHT:
            if not self.thrust_player or not self.thrust_player.playing:
                self.thrust_player = arcade.play_sound(self.thrust_sound)
            self.left = False
            self.right = True
            self.xidle = False
        elif key == arcade.key.UP:
            if not self.thrust_player or not self.thrust_player.playing:
                self.thrust_player = arcade.play_sound(self.thrust_sound)
            self.up = True
            self.down = False
        elif key == arcade.key.DOWN:
            if not self.thrust_player or not self.thrust_player.playing:
                self.thrust_player = arcade.play_sound(self.thrust_sound)
            self.down = True
            self.up = False

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT:
            self.left = False
            self.xidle = True
        elif key == arcade.key.RIGHT:
            self.right = False
            self.xidle = True
        elif key == arcade.key.UP:
            self.up = False
        elif key == arcade.key.DOWN:
            self.down = False

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()