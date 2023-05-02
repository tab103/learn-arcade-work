""" Lab 7 - User Control """

import arcade
import background

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

# class to draw sun
class Sun:
    def __init__(self, position_x, position_y, radius, color):
        """Sun class constructor"""
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        background.sun(self.position_x, self.position_y)

class moon:
    def __init__(self, position_x, position_y,change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.wall = arcade.load_sound("Lab 07 - User Control\wall.mp3")
        self.sound = None

    def render(self):
        background.moon(self.position_x, self.position_y, 10)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 10+self.radius:
            self.position_x = 10+self.radius

        if self.position_x > SCREEN_WIDTH - (10+self.radius):
            self.position_x = SCREEN_WIDTH - (10+self.radius)

        if self.position_y < 10+self.radius:
            self.position_y = 10+self.radius

        if self.position_y > SCREEN_HEIGHT - (10+self.radius):
            self.position_y = SCREEN_HEIGHT - (10+self.radius)

        # play sound if colliding with wall via x parameter
        if self.position_x == 10+self.radius or self.position_x == SCREEN_WIDTH - (10+self.radius) or self.position_y == 10+self.radius or self.position_y == SCREEN_HEIGHT - (10+self.radius):
            if not self.sound or not self.sound.playing:
                self.sound = arcade.play_sound(self.wall)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # make the cursor invisible
        self.set_mouse_visible(False)

        # draw the Sun
        self.Sun = Sun(50,50, 18, arcade.color.RED)
        self.moon = moon(100, 100, 0, 0, 10)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        # draw the background
        background.draw()

        self.Sun.draw()
        self.moon.render()
    def update(self, delta_time):
        self.moon.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.Sun.position_x = x
        self.Sun.position_y = y

    def on_key_press(self, key, modifiers):
        self.click=arcade.load_sound("Lab 07 - User Control\clicks.wav")
        if key == arcade.key.LEFT:
            self.moon.change_x = -MOVEMENT_SPEED
            arcade.play_sound(self.click)
        elif key == arcade.key.RIGHT:
            self.moon.change_x = MOVEMENT_SPEED
            arcade.play_sound(self.click)
        elif key == arcade.key.UP:
            self.moon.change_y = MOVEMENT_SPEED
            arcade.play_sound(self.click)
        elif key == arcade.key.DOWN:
            self.moon.change_y = -MOVEMENT_SPEED
            arcade.play_sound(self.click)
        elif key == arcade.key.SPACE:
            self.moon.change_x = 0
            self.moon.change_y = 0

def main():
    window = MyGame()
    arcade.run()

main()