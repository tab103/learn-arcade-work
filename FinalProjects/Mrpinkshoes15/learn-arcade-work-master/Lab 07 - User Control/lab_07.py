import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3
class Eye:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def draw_eye(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius + 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius + 10, arcade.csscolor.BLUE)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.position_x + 150, self.position_y, self.radius + 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(self.position_x + 150, self.position_y, self.radius + 10, arcade.csscolor.BLUE)
        arcade.draw_circle_filled(self.position_x + 150, self.position_y, self.radius, arcade.csscolor.BLACK)

class Smile():
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw_smile(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y - 60, self.radius, self.color)
        arcade.draw_arc_filled(self.position_x, self.position_y, 200, 100, arcade.csscolor.RED, 180, 360)
        arcade.draw_arc_filled(self.position_x, self.position_y - 5, 180, 80, arcade.csscolor.DARK_RED, 180, 360)
        arcade.draw_arc_filled(self.position_x, self.position_y - 30, 100, 200, arcade.csscolor.LIGHT_PINK, 180, 360)
        arcade.draw_arc_filled(self.position_x - 20, self.position_y - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)
        arcade.draw_arc_filled(self.position_x + 20, self.position_y - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.smile = Smile(50, 50, 0, 0, 30, arcade.color.AUBURN)
        # Create our eyes
        self.eye = Eye(50, 50, 15, arcade.csscolor.BLACK)
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_circle_filled(320, 240, 120, arcade.csscolor.GREEN)
        self.smile.draw_smile()
        self.eye.draw_eye()

    def update(self, delta_time):
        self.smile.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.smile.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.smile.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.smile.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.smile.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.smile.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.smile.change_y = 0
    def on_mouse_press(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.eye.position_x = x
        self.eye.position_y = y
        self.eye.radius -= 30

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.eye.radius += 30

def main():
    window = MyGame(640, 480, "lab 7")
    arcade.run()


main()