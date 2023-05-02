import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
COIN_COUNT = 150
# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 10


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

        self.coin_list = None
        self.all_sprites_list = None

        # list for wall blocks
        self.multiples_of_64_list = [320, 384, 448, 512]
        self.score = 0
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
        self.coin_list = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("../Testing/piderman.png",
                                           scale=0.04)
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

         ### Set up walls with random empty spaces
        for y in range(136, 1650, 128):
            for x in range(0, 2560, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        # makes random choice based on a list
        # creates random path blockers
        c = random.choice(self.multiples_of_64_list)
        for y in range(200, 1650, c):
            for x in range(192, 2560, c):
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        ### left and right boarders
        for side_boarders_y in range(8, 1694, 64):
            for side_position_x in range(-64, 2528, 2560):
                side_boarder = arcade.Sprite("../Testing/kekw.png", 0.1)
                side_boarder.center_x = side_position_x
                side_boarder.center_y = side_boarders_y
                self.wall_list.append(side_boarder)

        ## top and bottom boarders
        for top_boarders_x in range(0, 2560, 64):
            for top_position_y in range(8, 1694, 1664):
                top_boarder = arcade.Sprite("../Testing/kekw.png", 0.1)
                top_boarder.center_x = top_boarders_x
                top_boarder.center_y = top_position_y
                self.wall_list.append(top_boarder)

        ### coins loopings
        for coins in range(COIN_COUNT):
            coin = arcade.Sprite("cat_coin_3.png", 0.05)
        # Set the background color
            coins_placed_successfully = False

            while not coins_placed_successfully:
                coin.center_x = random.randrange(2432)
                coin.center_y = random.randrange(1664)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coins_placed_successfully = True
            self.coin_list.append(coin)





    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()


        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()


        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()


        # Draw the GUI
        # arcade.draw_rectangle_filled(self.width // 2,
        #                              20,
        #                              self.width,
        #                              40,
        #                              arcade.color.ALMOND)
        # text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
        #        f"{self.camera_sprites.position[1]:5.1f})"
        # arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 18)
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

        ### scoring
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10

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