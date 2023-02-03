import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_triangle(x, y, scale):
    """function to draw a triangle at the specified location"""
    # base triangle is 2 pixels wide and 2 pixels high. The coordinates x and y mark the center.
    point_list = [(x - scale, y - scale), (x + scale, y - scale), (x , y + scale)] # list of tuples

    """
    def draw_polygon_filled(point_list: Sequence[tuple[float, float] | list[float]],
                        color: tuple[int, int, int] | list[int] | tuple[int, int, int, int])
    Draw a polygon that is filled in.  
        Params:
        point_list – List of points making up the lines. Each point is in a list. So it is a list of lists.
        color – The color, specified in RGB or RGBA format.
    
    Note: I used polygon because that will be the easiest way for you to create stars
    """

    arcade.draw_polygon_filled(point_list, arcade.csscolor.WHITE) # draw a polygon by specifying the points

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Random Triangles")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

# create 50 triangles randomly placed on the screen
for s in range(1,50):
    random_x = random.randint(20, SCREEN_WIDTH - 20) # random x-coordinate between 20 and 780
    random_y = random.randint(20, SCREEN_HEIGHT - 20) # random y-coordinate between 20 and 580
    size = random.randint(1, 10)    # size range from zero to 10
    draw_triangle(random_x,random_y,size)

#  Finish and run
arcade.finish_render()
arcade.run()