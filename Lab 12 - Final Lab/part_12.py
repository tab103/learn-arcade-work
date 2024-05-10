import arcade

SPRITE_SCALING = 2
TILE_SCALING = 1
GRID_PIXEL_SIZE = 18
GRAVITY = 0.25

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab"
VIEWPORT_MARGIN = 50
CAMERA_SPEED = 0.1
MOVEMENT_SPEED = 5
JUMP = 5


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title, resizable=True)
        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.score = arcade.load_sound("TownTheme.mp3")  # https://opengameart.org/content/town-theme-rpg
        self.score_player = None
        self.walk = arcade.load_sound("sfx_step_grass_l.flac")  # https://opengameart.org/content/grass-foot-step-sou
        # nds-yo-frankie
        self.walk_player = None
        self.jump = arcade.load_sound("SFX_Jump_01.wav")  # https://opengameart.org/content/8-bit-jump-1
        self.jump_player = None
        self.player_sprite = None
        self.physics_engine = None
        self.left_pressed = False
        self.right_pressed = False
        self.tile_map = None
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("FinalLabPlayer.png",
                                           scale=1)
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 20
        self.player_list.append(self.player_sprite)
        map_name = "FinalLab1.tmj"
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)
        self.wall_list = self.tile_map.sprite_lists["Ground"]
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            self.wall_list,
            gravity_constant=GRAVITY
        )

    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        self.wall_list.draw()
        self.player_list.draw()
        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP
                if not self.jump_player or not self.jump_player.playing:
                    self.jump_player = arcade.play_sound(self.jump)
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.player_sprite.change_x = 0
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            if not self.walk_player or not self.walk_player.playing:
                self.walk_player = arcade.play_sound(self.walk)
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
            if not self.walk_player or not self.walk_player.playing:
                self.walk_player = arcade.play_sound(self.walk)
        if not self.score_player or not self.score_player.playing:
            self.score_player = arcade.play_sound(self.score)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a
        smoother pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
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
