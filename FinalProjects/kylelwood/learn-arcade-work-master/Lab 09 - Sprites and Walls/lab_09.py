

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING_BOX = 3.75
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COINS = .025
COIN_COUNT = 35
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "2D Platform Scroller"
VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 3.5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # player
        self.player_sprite = None

        # Set score
        self.score = 0

        # Physics engine
        self.physics_engine = None

        # keypress
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # camera
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # sounds from pixabay
        self.coin_collected = arcade.load_sound("collectcoin-6075.mp3")

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("player_idle.png", scale=0.4)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 0
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        # tile from kenny.nl
        for x in range(200, 1600, 365):
            for y in range(200, 1600, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(10) > 0:
                    wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for y in range(200, 1600, 365):
            for x in range(200, 1600, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(10) > 0:
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

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from pixabay.com
            coin = arcade.Sprite("coin-1753248_1280.png", SPRITE_SCALING_COINS)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(200, 1650)
                coin.center_y = random.randrange(0, 1600)

                # check for collision with wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # check for collision with other coins
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.PASTEL_ORANGE)

    def update(self, delta_time):
        self.coin_list.update()
        self.player_list.update()

        # list of all sprites that collide with the player.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collected)
            self.score += 1

    def on_draw(self):
        self.clear()

        # Select the camera
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the camera for GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        output = "Coins Collected / 35: " + str(self.score)
        arcade.draw_text(output, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):

        # Calculate speed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites
        self.physics_engine.update()

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
