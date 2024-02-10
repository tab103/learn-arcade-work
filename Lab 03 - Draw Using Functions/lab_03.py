# import arcade module
import arcade
import arcade.color

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_ground():
    """Draws Ground"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, (51, 47, 38))


def draw_moon():
    """Draws the Crescent Moon"""
    arcade.draw_circle_filled(400, 500, 60, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(420, 500, 60, arcade.csscolor.BLACK)


def draw_building(x, y):
    """Draws building"""
    arcade.draw_rectangle_filled(x, y-10, 180, 180, (103, 108, 115))
    arcade.draw_rectangle_filled(x-70, y-80, 20, 40, (42, 52, 66))
    arcade.draw_rectangle_filled(x-30, y-75, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x+20, y-75, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x-30, y-25, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x+20, y-25, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x-70, y-25, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x-30, y+25, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x+20, y+25, 20, 20, (199, 175, 80))
    arcade.draw_rectangle_filled(x-70, y+25, 20, 20, (199, 175, 80))
    arcade.draw_circle_filled(x-63, y-83, 3, (0, 0, 0))


def draw_stars(x, y):
    arcade.draw_circle_filled(x, y, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-20, y+20, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+20, y-20, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-50, y-30, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+50, y+30, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-50, y+30, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+50, y-30, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+20, y+20, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-20, y-20, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-50, y, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x, y-30, 2, arcade.csscolor.WHITE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Round 2")
    arcade.set_background_color((0, 0, 0))
    arcade.start_render()
    draw_stars(200, 500)
    draw_stars(300, 500)
    draw_stars(300, 300)
    draw_stars(150, 400)
    draw_ground()
    draw_moon()
    draw_building(150, 300)
    draw_building(450, 300)

    # End Drawing
    arcade.finish_render()

    # Keeps window open until someone closes it
    arcade.run()


main()
