import arcade
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALE = 0.4

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Update beach ball
    on_draw.x += on_draw.x_increment
    on_draw.y += on_draw.y_increment
    if on_draw.x > SCREEN_WIDTH or on_draw.x < 0:
        on_draw.x_increment = -on_draw.x_increment
        on_draw.rotation_increment = random.randint(-10, 10)
    if on_draw.y > SCREEN_HEIGHT or on_draw.y < 0:
        on_draw.y_increment = -on_draw.y_increment
        on_draw.rotation_increment = random.randint(-10, 10)
    on_draw.rotation += on_draw.rotation_increment
    if on_draw.rotation == 360:
        on_draw.rotation = 0  # handle overflows

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 1
    if (on_draw.snow_person1_x == 600):
        on_draw.snow_person1_x = 0

    # draw beach ball
    arcade.draw_scaled_texture_rectangle(on_draw.x, on_draw.y, on_draw.ball_texture, SCALE, on_draw.rotation)


# create on_draw function attributes
on_draw.ball_texture = arcade.load_texture("beach-ball.png")
on_draw.x = random.randint(0,700)
on_draw.y = random.randint(0,700)
on_draw.x_increment = random.randint(-5,5)
on_draw.y_increment = random.randint(-8,8)
on_draw.rotation_increment = random.randint(5,10)
on_draw.rotation = 0

# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()