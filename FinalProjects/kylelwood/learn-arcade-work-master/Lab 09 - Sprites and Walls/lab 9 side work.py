""" Sprite Sample Program """

import arcade

# --- Constants ---
# Box = 20 pixels
SPRITE_SCALING_BOX = 2.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("player_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
        wall.center_x = 320
        wall.center_y = 200
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite("tile_0000.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()