import random
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

VIEWPORT_MARGIN = 0

CAMERA_SPEED = 0.1

CHARACTER_SCALING = .75
SPRITE_SCALING = .5
SPRITE_SCALING_WALLS = .5

PLAYER_MOVEMENT_SPEED = 2
MOVEMENT_SPEED = 2
GRAVITY = 1.2

PLAYER_JUMP_SPEED = 15
font_size = 20


class Wall(arcade.Sprite):
    def __init__(self, image, scale, game):
        super().__init__(image, scale)
        self.game = game

    def update(self):
        """ Move the walls """
        # Move walls.
        # Remove these lines if physics engine is moving walls.
        self.center_x += self.game.wall_change_x


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

        self.image = None
        self.fly_plane = None
        self.scene = None

        self.player_list = None
        self.walls_list = None
        self.score = 0

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.walls_sprite = None
        # Our physics engine
        self.physics_engine = None

        self.set_mouse_visible(True)
        self.space_pressed = False
        self.game_started = False
        self.game_over = False
        self.monitor = 0
        self.wall_change_x = 0

        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        self.wall_set = []
        self.wall_set.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
        self.wall_set.append([1, 0, 0, 0, 1, 1, 1, 1, 1, 1])
        self.wall_set.append([1, 1, 0, 0, 0, 1, 1, 1, 1, 1])
        self.wall_set.append([1, 1, 1, 0, 0, 0, 1, 1, 1, 1])
        self.wall_set.append([1, 1, 1, 1, 0, 0, 0, 1, 1, 1])
        self.wall_set.append([1, 1, 1, 1, 1, 0, 0, 0, 1, 1])
        self.wall_set.append([1, 1, 1, 1, 1, 1, 0, 0, 0, 1])
        self.wall_set.append([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])

    def generate_walls(self):
        random_wall = random.randint(0, 7)
        ndx = 10
        for y in range(32, 640, 64):
            ndx -= 1
            if self.wall_set[random_wall][ndx] == 0:
                continue
            wall_segment = Wall(":resources:images/tiles/brickGrey.png", SPRITE_SCALING_WALLS, self)
            wall_segment.center_x = SCREEN_WIDTH + 64
            wall_segment.center_y = y
            self.walls_list.append(wall_segment)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.scene = arcade.Scene()
        # Sprite lists
        self.player_list = arcade.SpriteList()

        self.score = 0

        self.walls_list = arcade.SpriteList()
        self.generate_walls()

        # self.flying_plane = [arcade.Sprite("planeGreen1.png", CHARACTER_SCALING),
        #                      arcade.Sprite("planeGreen2.png", CHARACTER_SCALING),
        #     arcade.Sprite("planeGreen3.png", CHARACTER_SCALING)]
        # # for i in range(self.flying_plane):
        # #     image_source = i
        self.fly_plane = []
        self.fly_plane.append(arcade.Sprite("planeGreen1.png", CHARACTER_SCALING))
        self.fly_plane.append(arcade.Sprite("planeGreen2.png", CHARACTER_SCALING))
        self.fly_plane.append(arcade.Sprite("planeGreen3.png", CHARACTER_SCALING))
        self.fly_plane.append(arcade.Sprite("planeRed1.png", CHARACTER_SCALING))
        self.fly_plane.append(arcade.Sprite("planeRed2.png", CHARACTER_SCALING))
        self.fly_plane.append(arcade.Sprite("planeRed3.png", CHARACTER_SCALING))
        self.image = 0

        self.player_sprite = self.fly_plane[self.image]


        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(

            self.player_sprite, self.walls_list, gravity_constant=GRAVITY)

    def update_walls_speed(self):
        if self.space_pressed:
            self.wall_change_x -= MOVEMENT_SPEED
            self.monitor += MOVEMENT_SPEED
            if self.monitor > SCREEN_WIDTH / 3:
                self.generate_walls()
                self.monitor = 0

        for seg in self.walls_list:
            if seg.center_x < 0:
                seg.remove_from_sprite_lists()

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        arcade.start_render()

        self.walls_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 350, 20, arcade.color.BLACK, font_size)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
            self.game_started = True
            self.space_pressed = True

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.image += 1
        # if self.image >= len(self.fly_plane):
        #     self.image = 0
        # self.player_sprite = self.fly_plane[self.image]

        self.update_walls_speed()
        self.walls_list.update()
        self.wall_change_x = 0

        if not arcade.check_for_collision_with_list(self.player_sprite, self.walls_list):
            self.game_over = False
            self.score += 1

        if arcade.check_for_collision_with_list(self.player_sprite, self.walls_list):
            print("game over")

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
