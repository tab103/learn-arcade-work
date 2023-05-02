"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
ROCK_COUNT = 30
SPRITE_SCALING_ROCK = 0.3

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
        self.rock_list = None
        self.wall_hit_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # loading sound
        self.metalpot = arcade.load_sound("metalPot1.ogg")

        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.wall_hit_list = arcade.SpriteList()
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("robot_greenDrive2.png",
                                           scale=0.2)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)



        # -- Set up several columns and rows of walls
        for x in range(200, 900, 110):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)
        for x in range(900, 800, 110):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)
        for x in range(430, 700, 110):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 555
            self.wall_list.append(wall)
        for x in range(450, 750, 110):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 450
            self.wall_list.append(wall)
            # X-axis outside wall
        for x in range(-100, 1200, 110):
            wall = arcade.Sprite("elementStone032.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)
        for x in range(-100, 1200, 110):
            wall = arcade.Sprite("elementStone032.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1010
            self.wall_list.append(wall)
        for y in range(300, 900, 80):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = 100
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(705, 800, 40):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = 300
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(555, 900, 40):
            wall = arcade.Sprite("elementExplosive016.png", SPRITE_SCALING)
            wall.center_x = 900
            wall.center_y = y
            self.wall_list.append(wall)
            # y-axis outside wall
        for y in range(170, 1000, 110):
            wall = arcade.Sprite("elementStone041.png", SPRITE_SCALING)
            wall.center_x = -140
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(170, 1000, 110):
            wall = arcade.Sprite("elementStone041.png", SPRITE_SCALING)
            wall.center_x = 1150
            wall.center_y = y
            self.wall_list.append(wall)

            for i in range(ROCK_COUNT):
                rock = arcade.Sprite("rock.png", SPRITE_SCALING_ROCK)
                # position rocks

                placed = False

                while not placed:
                    rock.center_x = random.randrange(-100, 1100)
                    rock.center_y = random.randrange(110, 920)
                    # add to list

                    wall_hit_list = arcade.check_for_collision_with_list(rock, self.wall_list)
                    if len(wall_hit_list) == 0:
                        placed = True

                self.rock_list.append(rock)

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.rock_list.draw()

        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()

        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=50,
                         color=arcade.color.WHITE, font_size=14)

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
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

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player

        self.scroll_to_player()

        # checking for collision and loading sound
        rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)

        for rock in rock_hit_list:
            rock.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.metalpot)

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
