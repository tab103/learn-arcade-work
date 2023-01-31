import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
xcoord = 150

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
    #global xcoord
    #draw_snow_person(xcoord, 140)

    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 5
    #xcoord = xcoord + 5
    if on_draw.snow_person1_x == 800:
        on_draw.snow_person1_x = 0


# Create a value that our on_draw.snow_person1_x will start at.
# this is a function attribute (i.e. we added a variable to the on_draw function
on_draw.snow_person1_x = 150

def main():
    # creates window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

    # set color
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    # creates a refresh schedule where everything in the on_draw function is done 60 times per second.
    arcade.schedule(on_draw, 1/60)

    # background run loop
    arcade.run()


# Call the main function to get the program started.
main()