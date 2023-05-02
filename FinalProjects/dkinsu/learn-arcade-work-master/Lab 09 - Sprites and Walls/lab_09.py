"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 8
RING_COUNT = 20
SPRITE_SCALING_RING = 1.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.ring_list = None
        self.score = 0
        # Setting up sound, vine boom noise
        self.vine_boom = arcade.load_sound("vine-boom.wav")

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.ring_list = arcade.SpriteList()

        # Set up the player - from Kenney.nl micro roguelike
        self.player_sprite = arcade.Sprite("tile_0004.png",
                                           scale=8)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Kenney.nl micro roguelike ring sprite
        self.ring = arcade.Sprite("tile_0089.png", SPRITE_SCALING_RING)

        # -- Set up border rows of walls - top and bottom

        # All sprites used are from Kenney.nl Micro roguelike
        for x in range(0, 1200, 64):
            x_wall = arcade.Sprite("tile_0001.png", SPRITE_SCALING)
            x_wall.center_x = x
            x_wall.center_y = 200
            self.wall_list.append(x_wall)
        for x in range(0, 1200, 64):
            top_x_wall = arcade.Sprite("tile_0001.png", SPRITE_SCALING)
            top_x_wall.center_x = x
            top_x_wall.center_y = 1224
            self.wall_list.append(top_x_wall)
        # Left and right walls
        for y in range(200, 1200, 64):
            l_wall = arcade.Sprite("tile_0109.png", SPRITE_SCALING)
            l_wall.center_x = 0
            l_wall.center_y = y
            self.wall_list.append(l_wall)
        for y in range(200, 1264, 64):
            r_wall = arcade.Sprite("tile_0109.png", SPRITE_SCALING)
            r_wall.center_x = 1200
            r_wall.center_y = y
            self.wall_list.append(r_wall)

        # Border walls set up: setting up maze walls
        for x in range(64, 464, 64):
            maze_wall_1 = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            maze_wall_1.center_x = x
            maze_wall_1.center_y = 400
            self.wall_list.append(maze_wall_1)
        for x in range(628, 1170, 64):
            maze_wall_2 = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            maze_wall_2.center_x = x
            maze_wall_2.center_y = 400
            self.wall_list.append(maze_wall_2)
        for y in range(400, 1100, 64):
            maze_wall_3 = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            maze_wall_3.center_x = 200
            maze_wall_3.center_y = y
            self.wall_list.append(maze_wall_3)
        for x in range(428, 1160, 64):
            maze_wall_4 = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            maze_wall_4.center_x = x
            maze_wall_4.center_y = 700
            self.wall_list.append(maze_wall_4)
        for y in range(628, 1100, 64):
            maze_wall_5 = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            maze_wall_5.center_x = 800
            maze_wall_5.center_y = y
            self.wall_list.append(maze_wall_5)
        # adding wall made by list, formation of boxes
        box_list = [[1050, 840], [1050, 776], [986, 840], [986, 776]]
        for box in box_list:
            box_wall = arcade.Sprite("tile_0151.png", SPRITE_SCALING)
            box_wall.center_x = box[0]
            box_wall.center_y = box[1]
            self.wall_list.append(box_wall)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        ring_placed_successfully = False

        while not ring_placed_successfully:
            for i in range(RING_COUNT):
                self.ring.center_x = random.randrange(1200)
                self.ring.center_y = random.randrange(1200)

                # Check for wall collision
                wall_hit_list = arcade.check_for_collision_with_list(self.ring, self.wall_list)

                # See if the ring is hitting another ring
                ring_hit_list = arcade.check_for_collision_with_list(self.ring, self.ring_list)

                if len(wall_hit_list) == 0 and len(ring_hit_list) == 0:
                    # It is!
                    ring_placed_successfully = True

        # Add the ring to the lists

        self.ring_list.append(self.ring)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.ring_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Score: {self.score}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
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

        rings_hit_lists_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                        self.ring_list)
        for ring in rings_hit_lists_hit_list:
            ring.remove_from_sprite_lists()
            arcade.play_sound(self.vine_boom, 0.6)
            self.score += 1

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
