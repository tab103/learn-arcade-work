""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 8


class Shape:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        arcade.draw_triangle_filled(self.position_x - 20, self.position_y - 20, self.position_x + 20, self.position_y -
                                    20, self.position_x, self.position_y, self.color)
        arcade.draw_triangle_filled(self.position_x - 20, self.position_y + 20, self.position_x + 20, self.position_y +
                                    20, self.position_x, self.position_y, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x


class Shape2:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.bounce = arcade.load_sound("bounce.wav")
        self.bounce_player = None

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.csscolor.WHITE)
        # To make it a Crescent
        arcade.draw_circle_filled(self.position_x + 20, self.position_y, self.radius, arcade.csscolor.BLACK)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y
        if self.position_x < self.radius:
            self.position_x = self.radius
            if not self.bounce_player or not self.bounce_player.playing:
                self.bounce_player = arcade.play_sound(self.bounce)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            if not self.bounce_player or not self.bounce_player.playing:
                self.bounce_player = arcade.play_sound(self.bounce)

        if self.position_y < self.radius:
            self.position_y = self.radius
            if not self.bounce_player or not self.bounce_player.playing:
                self.bounce_player = arcade.play_sound(self.bounce)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            if not self.bounce_player or not self.bounce_player.playing:
                self.bounce_player = arcade.play_sound(self.bounce)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        self.shape = Shape(20, 20, 0, 0, arcade.color.VIOLET)
        self.shape2 = Shape2(400, 400, 0, 0, 30)
        self.song = arcade.load_sound("song.wav")
        self.song_player = None

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, (51, 47, 38))
        arcade.draw_rectangle_filled(150, 300 - 10, 180, 180, (103, 108, 115))
        arcade.draw_rectangle_filled(150 - 70, 300 - 80, 20, 40, (42, 52, 66))
        arcade.draw_rectangle_filled(150 - 30, 300 - 75, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 + 20, 300 - 75, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 - 30, 300 - 25, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 + 20, 300 - 25, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 - 70, 300 - 25, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 - 30, 300 + 25, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 + 20, 300 + 25, 20, 20, (199, 175, 80))
        arcade.draw_rectangle_filled(150 - 70, 300 + 25, 20, 20, (199, 175, 80))
        arcade.draw_circle_filled(150 - 63, 300 - 83, 3, (0, 0, 0))
        self.shape.draw()
        self.shape2.draw()

    def update(self, delta_time):
        self.shape.update()
        self.shape2.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.shape.position_x = x
        self.shape.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.song_player or not self.song_player.playing:
                self.song_player = arcade.play_sound(self.song)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            if not self.song_player or not self.song_player.playing:
                self.song_player = arcade.play_sound(self.song)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.shape2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.shape2.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.shape2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.shape2.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.shape2.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.shape2.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
