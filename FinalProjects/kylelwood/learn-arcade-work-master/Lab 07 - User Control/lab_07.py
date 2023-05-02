""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "FLYING COIN RACE"

CHARACTER_SCALING = 1
MOVEMENT_SPEED = 2.5


def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename, flipped_horizontally=True)]


class FighterPlane:
    """2 planes that will fly on screen"""
    def __init__(self, position_x, position_y, change_x, change_y, size, image):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size
        self.image = image

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        self.fly_texture_pair = load_texture_pair(self.image)

        self.texture = self.fly_texture_pair[0]

        self.engine_noise = arcade.load_sound("prop-plane-14513.mp3")
        arcade.play_sound(self.engine_noise)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.size:
            self.position_x = self.size

        if self.position_x > SCREEN_WIDTH - 50:
            self.position_x = SCREEN_WIDTH - 50

        if self.position_y < self.size:
            self.position_y = self.size

        if self.position_y > SCREEN_HEIGHT - 50:
            self.position_y = SCREEN_HEIGHT - 50

    def myupdate_animation(self):
        if self.change_y > 0:
            self.texture = self.fly_texture_pair[0]
        elif self.change_y < 0:
            self.texture = self.fly_texture_pair[1]

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.position_x, self.position_y, 55, 55, self.fly_texture_pair[0])


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE)

        self.set_mouse_visible(False)

        self.player1 = FighterPlane(700, 500, 0, 0, 5, "biplane-158327_1280.png")
        self.player2 = FighterPlane(50, 500, 0, 0, 5, "green-304704_640.png")

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BURNT_ORANGE)
        self.draw_sun()
        self.draw_sea()
        self.draw_sailboat(150, 21)
        self.player1.draw()
        self.player2.draw()

    def update(self, delta_time):
        self.player1.update()
        self.player2.update()

    def draw_sun(self):
        # draw the sun
        arcade.draw_circle_filled(400, 165, 150, arcade.color.SUNRAY)

    def draw_sea(self):
        # draw the sea
        arcade.draw_lrtb_rectangle_filled(0, 800, 70, 0, arcade.color.HONOLULU_BLUE)

    def draw_sailboat(self, x, y):
        # draw a sailboat
        arcade.draw_lrtb_rectangle_filled(380 + x, 420 + x, 60 + y, 50 + y, arcade.color.BLACK)
        arcade.draw_triangle_filled(390 + x, 65 + y, 410 + x, 65 + y, 400 + x, 80 + y, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(399 + x, 401 + x, 70 + y, 50 + y, arcade.color.BLACK)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player1.change_y = -MOVEMENT_SPEED

        if key == arcade.key.A:
            self.player2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player2.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player2.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player1.change_y = 0

        if key == arcade.key.A or key == arcade.key.D:
            self.player2.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player2.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
