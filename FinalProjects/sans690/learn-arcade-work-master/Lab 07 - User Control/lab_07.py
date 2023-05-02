""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

# defines the laser sound based the files that is given from the location on the computer
laser_sound = arcade.load_sound("laser.wav", False)
mouse_click_sound = arcade.load_sound("arcade_resources_sounds_hurt1.wav")


# creates the class Hat
class Hat:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        # attributes to the class Hat
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    # method that creates the hat structure and assigns some values to width and height
    def draw(self):
        # top part of the hat
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 40, 50, self.color)
        # bottom part of the hat
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 20, 60, 10, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 40, 10, arcade.color.WHITE)

    # method that update movement class Hat
    def update(self):
        # when the x position of Hat changes, it effects the x current position of Hat
        # when change_x is added to the position_x the Hat moves from current position to new position
        # stores that new position as the position_x
        self.position_x += self.change_x
        # when the y position of Hat changes, it effects the y current position of Hat
        # when change_y is added to the position_y the face instance moves from current position to new position
        # stores that new position as the position_y
        self.position_y += self.change_y

        # detects where the screen ends and stops Hat instance from moving past limit
        # keeps hat from moving past limit of window to the left on x-axis
        if self.position_x < 30:
            self.position_x = 30
        # keeps hat from moving past limit of window to the right on x-axis
        elif self.position_x > SCREEN_WIDTH - 30:
            # set the position_y = SCREEN_WIDTH - 30
            self.position_x = SCREEN_WIDTH - 30
        # keeps hat from moving past limit of window downward on y-axis
        elif self.position_y < 25:
            # set position_y equal to 25
            self.position_y = 25
        # keeps hat from moving past limit of window upward on y-axis
        elif self.position_y > SCREEN_HEIGHT - 25:
            self.position_y = SCREEN_HEIGHT - 25


# create the class Face
class Face:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # attributes of the class Face
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    # method creates the structure for the class Face
    # this method steals the values from where the face instance is created in the MyGame class
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        # creates the eyes
        arcade.draw_circle_filled(self.position_x - 10, self.position_y, 4.5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 10, self.position_y, 4.5, arcade.color.BLACK)
        # creates the mouth
        arcade.draw_arc_outline(self.position_x, self.position_y - 7, SCREEN_WIDTH / 60, SCREEN_HEIGHT / 40,
                                arcade.color.BLACK, 190, 360, 4.5)

    # method that defines the movement of the Face
    def update(self):
        # when the x position of Face changes, it effects the x current position of Face
        # when change_x is added to the position_x Face moves from current position to new position
        # stores that new position as the position_x
        self.position_x += self.change_x
        # when the y position of Face changes, it effects the y current position of Face
        # when change_y is added to the position_y Face moves from current position to new position
        # stores that new position as the position_y
        self.position_y += self.change_y

        # detects where the screen ends and stops face instance from moving past limit
        # when limit is hit a sound will play
        # keeps face from moving past limit of window to the left on x-axis
        if self.position_x < self.radius:
            arcade.play_sound(laser_sound)
            self.position_x = self.radius
        # keeps face from moving past limit of window to the right on x-axis
        elif self.position_x > SCREEN_WIDTH - self.radius:
            arcade.play_sound(laser_sound)
            self.position_x = SCREEN_WIDTH - self.radius
        # keeps face from moving past limit of window downward on y-axis
        elif self.position_y < self.radius:
            arcade.play_sound(laser_sound)
            self.position_y = self.radius
        # keeps face from moving past limit of window upward on y-axis
        elif self.position_y > SCREEN_HEIGHT - self.radius:
            arcade.play_sound(laser_sound)
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # creates an instances of class Face and Hat while also assigning it values to its parameters
        self.face = Face(200, 300, 0, 0, 25, arcade.color.YELLOW)
        self.hat = Hat(400, 300, 0, 0, arcade.color.BLACK)

        # makes the mouse arrow invisible in class MyGame window
        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        # sets background color from library
        arcade.set_background_color(arcade.color.BLUE)

        # creates grass
        # left of 0, right 799
        # top of 200, bottom 0
        arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, arcade.color.GO_GREEN)

        # creates house base
        # left 30, right 300
        # top of 200, bottom of 160
        arcade.draw_lrtb_rectangle_filled(30, 300, 200, 160, arcade.color.FAWN)

        # creates house base second color
        # left of 30, right of 300
        # top of 300, bottom 170
        arcade.draw_lrtb_rectangle_filled(30, 300, 300, 170, arcade.color.BONE)

        # creates house door
        # left of 145, right 185
        # top of 220, bottom of 160
        arcade.draw_lrtb_rectangle_filled(145, 185, 220, 160, arcade.color.BURNT_UMBER)

        # creates house window (left)
        # left of 70, right of 100
        # top of 230, bottom of 200
        arcade.draw_lrtb_rectangle_filled(70, 100, 230, 200, arcade.color.BROWN)

        # creates house window (right)
        # left of 230, right of 260
        # top of 230, bottom of 200
        arcade.draw_lrtb_rectangle_filled(230, 260, 230, 200, arcade.color.BROWN)

        # creates roof from triangle with 3 points
        # (10, 300) (170, 400) (315, 300)
        arcade.draw_triangle_filled(10, 300, 170, 400, 315, 300, arcade.color.BROWN)

        # creates lines on window (left)
        arcade.draw_line(65, 200, 105, 200, arcade.color.COCOA_BROWN, 3)

        # creates lines on window (right)
        arcade.draw_line(225, 200, 265, 200, arcade.color.COCOA_BROWN, 3)

        # creates inside window (left)
        arcade.draw_lrtb_rectangle_filled(75, 95, 225, 205, arcade.color.WHITE)

        # creates inside window (right)
        arcade.draw_lrtb_rectangle_filled(235, 255, 225, 205, arcade.color.WHITE)

        # creates lines inside window (left)
        # creates horizontal line
        arcade.draw_line(70, 215, 100, 215, arcade.color.BROWN, 2)
        # creates vertical line
        arcade.draw_line(85, 230, 85, 202, arcade.color.BROWN, 2)

        # creates lines inside window (right)
        # creates horizontal line
        arcade.draw_line(230, 215, 260, 215, arcade.color.BROWN, 2)
        # creates vertical line
        arcade.draw_line(245, 230, 245, 202, arcade.color.BROWN, 2)

        # creates tree trunk
        arcade.draw_rectangle_filled(500, 180, 30, 80, arcade.color.BROWN)
        # creates eaves for tree
        arcade.draw_circle_filled(500, 230, 50, arcade.color.GREEN)

        # calls face instance to start rendering it
        self.face.draw()
        self.hat.draw()

    # updates the class Face and Hat instances in class MyGame
    def update(self, delta_time):
        # self refers to the class
        self.face.update()
        self.hat.update()

    # method that determines when the user has a button pressed
    def on_key_press(self, key, modifiers):
        # the change in x is effected takes the value of constant movement speed
        # negative movement will move the face left when it equals the change in x
        if key == arcade.key.LEFT:
            self.face.change_x = -MOVEMENT_SPEED
        # if not left
        elif key == arcade.key.RIGHT:
            # the change in x is effected takes the value of constant movement speed
            # positive movement will move the face right when it equals the change in x
            self.face.change_x = MOVEMENT_SPEED
        # if not right or left
        elif key == arcade.key.DOWN:
            # the change in y is effected takes the value of constant movement speed
            # negative movement will move the face down when it equals the change in y
            self.face.change_y = -MOVEMENT_SPEED
        # if not down, right, or left
        elif key == arcade.key.UP:
            # the change in y is effected takes the value of constant movement speed
            # positive movement will move the face up when it equals the change in y
            self.face.change_y = MOVEMENT_SPEED

    # method defined in the MyGame
    # detects when the user releases the key
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            # the current x position does NOT change because there is no change to the change_x
            self.face.change_x = 0
        elif key == arcade.key.DOWN or key == arcade.key.UP:
            # the current y position does NOT change because there is no change to the change_y
            self.face.change_y = 0

    # moves the face based on mouse movement
    def on_mouse_motion(self, x, y, dx, dy):
        self.hat.position_x = x
        self.hat.position_y = y

    # if user clicks the left or right mouse button a sound will play
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(mouse_click_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(mouse_click_sound)


def main():
    window = MyGame()
    arcade.run()


main()
