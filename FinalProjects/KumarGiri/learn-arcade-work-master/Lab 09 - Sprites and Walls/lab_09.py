
import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
COIN_SCALING = 0.3
FENCE_SCALING = 0.8

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
COIN_COUNT = 50

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 6

# coin class
class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)
        # sounds
        self.coin_sound = arcade.load_sound("clicks.wav")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.boundary_list= None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # score
        self.score= 0

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.boundary_list= arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("images/player_idle.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        for x in range(200, 1550, 210):
            for y in range(70, 1520, 35):
                if random.randrange(4) == 2:
                    grass = arcade.Sprite("images/grass.png", SPRITE_SCALING)
                    grass.center_x = y
                    grass.center_y = x
                    self.wall_list.append(grass)
        list = [115, 540, 1150, 1380]
        for x in list:
            for y in range (70, 1450, 35):
                wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)
                wall.center_x = y
                wall.center_y = x
                self.wall_list.append(wall)

        # bottom fence
        for row in range(0,1600, 30):
            for column in range(1):
                boundary = arcade.Sprite("images/fenceLong.png", FENCE_SCALING)
                boundary.center_x = row
                boundary.center_y = column
                self.boundary_list.append(boundary)

        # left fence
        for row in range(0,1600, 30):
            for column in range(1):
                boundary = arcade.Sprite("images/fenceLong.png", FENCE_SCALING, flipped_diagonally=True, flipped_horizontally=True)
                boundary.center_x = column
                boundary.center_y = row
                self.boundary_list.append(boundary)

        # top fence
        for row in range(1):
            for column in range(0,1600, 30):
                boundary = arcade.Sprite("images/fenceLong.png", FENCE_SCALING, flipped_vertically=True)
                boundary.center_x = column
                boundary.center_y = 1600
                self.boundary_list.append(boundary)

        # right fence
        for row in range(0,1620, 30):
            for column in range(1):
                boundary = arcade.Sprite("images/fenceLong.png", FENCE_SCALING, flipped_diagonally=True)
                boundary.center_x = 1600
                boundary.center_y = row
                self.boundary_list.append(boundary)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, [self.wall_list, self.boundary_list])

        # draw coins
        for num in range(COIN_COUNT):
            self.coin = Coin("images\coin.png", COIN_SCALING)
            coin_placed_successfully = False
            while not coin_placed_successfully:

                # Position the coin
                self.coin.center_x = random.randrange(1600)
                self.coin.center_y = random.randrange(1600)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(self.coin, self.wall_list)
                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(self.coin, self.coin_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True
                    self.coin_list.append(self.coin)

        # Set the background color
        arcade.set_background_color(arcade.color.SAND_DUNE)

    def on_draw(self):
        """ Render the screen. """

        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.boundary_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        score_count = f"Score: {self.score}"
        arcade.draw_text(score_count,DEFAULT_SCREEN_WIDTH-150, 10, arcade.color.BLACK, 20)
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
        coin_hit_list= arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score+=1
            arcade.play_sound(self.coin_sound)

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
        position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
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