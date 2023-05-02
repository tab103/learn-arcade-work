import random
import arcade

# --- Constants ---
SPRITE_SCALING_WALLS = .5
MOVEMENT_SPEED = 3

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640


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
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.walls_list = None

        # Set up the walls info
        self.walls_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(True)
        self.space_pressed = False
        self.game_started = False
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
        self.walls_list = arcade.SpriteList()
        self.generate_walls()

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
        arcade.start_render()
        self.walls_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.game_started = True
            self.space_pressed = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.space_pressed = False

    def update(self, delta_time):
        self.update_walls_speed()
        self.walls_list.update()
        self.wall_change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
