"""To get the animation to work well, I needed to use OO techniques.
It won't make sense now but it will!"""

import random
import arcade
WIDTH = 900
HEIGHT = 900
SCALE = 0.3
SCREEN_TITLE = "Beachball Example"
BACKGROUND_COLOR = arcade.color.BLACK

"""Class representing a single beach ball"""
class beach_ball:
    def __init__(self):
        self.ball_texture = arcade.load_texture("beach-ball.png")
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,WIDTH)
        self.x_increment = random.randint(-5,5)
        self.y_increment = random.randint(-8,8)
        self.rotation_increment = random.randint(5,10)
        self.rotation = 0

    def update(self):
        self.x += self.x_increment
        self.y += self.y_increment
        if self.x > WIDTH or self.x < 0:
            self.x_increment = -self.x_increment
            self.rotation_increment = random.randint(-10,10)
        if self.y > HEIGHT or self.y < 0:
            self.y_increment = -self.y_increment
            self.rotation_increment = random.randint(-10,10)
        self.rotation += self.rotation_increment
        if self.rotation == 360:
            self.rotation = 0  # handle overflows

    def draw(self):
        arcade.draw_scaled_texture_rectangle(self.x, self.y, self.ball_texture, SCALE, self.rotation)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Create list of ball instances
        self.beach_balls = []
        for i in range(30):
            self.beach_balls.append(beach_ball())
        self.background_color = BACKGROUND_COLOR

    def on_update(self, delta_time):
        for i in range(30):
            self.beach_balls[i].update()

    def on_draw(self):
        self.clear()
        for i in range(30):
            self.beach_balls[i].draw()

def main():
    MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()