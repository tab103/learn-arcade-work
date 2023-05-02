""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Movement speed for key input
MOVEMENT_SPEED = 4
# ------------------

# Using cloud function from lab 3


class Cloud:
    def __init__(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

    def draw_cloud(self):
        # drawing a cloud, made with four ellipses
        arcade.draw_ellipse_filled(self.position_x - 30, self.position_y, self.width, self.height, self.color)
        arcade.draw_ellipse_filled(self.position_x, 15 + self.position_y, self.width, self.height, self.color)
        arcade.draw_ellipse_filled(30 + self.position_x, self.position_y, self.width, self.height, self.color)
        arcade.draw_ellipse_filled(self.position_x, self.position_y - 15, self.width, self.height, self.color)

# taking ball class from example and elaborating


class BigBall:
    def __init__(self, position_x, position_y, change_x, change_y, radius1, radius2, radius3, color1, color2, color3):

        self.error_sound = arcade.load_sound("arcade_resources_sounds_hurt2.wav")
        self.error_sound_player = None
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius1 = radius1
        self.radius2 = radius2
        self.radius3 = radius3
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def ball_draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius1, self.color1)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius2, self.color2)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius3, self.color3)

    def update(self):
        # Ball Movement
        self.position_y += self.change_y
        self.position_x += self.change_x
        # Edge of screen check
        if self.position_x < self.radius1:
            # Playing error sound on attempt to cross edge
            if not self.error_sound_player or not self.error_sound_player.playing:
                self.error_sound_player = arcade.play_sound(self.error_sound)
            self.position_x = self.radius1

        if self.position_x > SCREEN_WIDTH - self.radius1:
            if not self.error_sound_player or not self.error_sound_player.playing:
                self.error_sound_player = arcade.play_sound(self.error_sound)
            self.position_x = SCREEN_WIDTH - self.radius1

        if self.position_y < self.radius1:
            if not self.error_sound_player or not self.error_sound_player.playing:
                self.error_sound_player = arcade.play_sound(self.error_sound)
            self.position_y = self.radius1

        if self.position_y > SCREEN_HEIGHT - self.radius1:
            if not self.error_sound_player or not self.error_sound_player.playing:
                self.error_sound_player = arcade.play_sound(self.error_sound)
            self.position_y = SCREEN_HEIGHT - self.radius1


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.vine_boom = arcade.load_sound("vine-boom.wav")
        self.vine_boom_player = None

        # setting mouse invisible
        self.set_mouse_visible(False)

        # initializing cloud to be drawn
        self.cloud = Cloud(400, 300, 120, 45, arcade.color.WHITE)

        # initializing ball to be drawn
        self.ball = BigBall(200, 300, 0, 0, 40, 30, 20, arcade.color.BLUE, arcade.color.RED, arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()
        self.cloud.draw_cloud()
        self.ball.ball_draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.cloud.position_x = x
        self.cloud.position_y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.vine_boom_player or not self.vine_boom_player.playing:
                self.vine_boom_player = arcade.play_sound(self.vine_boom)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            if not self.vine_boom_player or not self.vine_boom_player.playing:
                self.vine_boom_player = arcade.play_sound(self.vine_boom)

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame()
    window.run()


main()
