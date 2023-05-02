#imports
import arcade

# screen stuff
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
x = 500
y = 375
def draw_ferrari():
        #front hood
    arcade.draw_arc_filled(524, 300, 530, 196, arcade.color.RED, 10, 160)
        #windows
    arcade.draw_arc_filled(585, 325, 400, 230, arcade.color.LIGHT_GRAY, 40, 180)
    arcade.draw_polygon_filled([(720, 410), (770, 388), (700, 388)], arcade.csscolor.LIGHT_GRAY)
        #rear/mid car body
    arcade.draw_polygon_filled([(780, 390), (430,375), (430, 305), (760, 305), (780, 310) ], arcade.csscolor.RED)
        #rear wing
    arcade.draw_polygon_filled([(838, 327), (780, 310), (780, 390), (795, 425), (838, 425)], arcade.csscolor.RED)
        #front spliter
    arcade.draw_polygon_filled([(430, 330), (275, 325), (270, 305), (430, 305)], arcade.csscolor.RED)
        #front fender
    arcade.draw_polygon_filled([(418,390), (450,375), (430, 330), (275, 325), (280, 338)], arcade.csscolor.RED)
        # A and B pillars
    arcade.draw_polygon_filled([(430, 375), (440, 375), (520, 429), (620, 429), (670, 396), (660, 385), (740, 388), (630, 437), (520, 437)], arcade.csscolor.RED)
        #wheel arches
    arcade.draw_arc_filled(385, 305, 105, 140, arcade.csscolor.DARK_RED, 0, 180)
    arcade.draw_arc_filled(740, 305, 105, 140, arcade.csscolor.DARK_RED, 8.30, 180)
        # wheels
    arcade.draw_ellipse_filled(385, 326, 90, 90, arcade.csscolor.BLACK, 0,)
    arcade.draw_ellipse_filled(740, 326, 92, 92, arcade.csscolor.BLACK, 0)
    arcade.draw_ellipse_filled(385, 326, 70, 70, arcade.csscolor.SILVER, 0,)
    arcade.draw_ellipse_filled(740, 326, 72, 72, arcade.csscolor.SILVER, 0)
        # side details
    arcade.draw_polygon_filled([(510, 372), (640, 378), (637, 350)], arcade.csscolor.DARK_RED)
    arcade.draw_polygon_filled([(600, 327), (665, 338), (663, 318)], arcade.csscolor.DARK_RED)
    arcade.draw_polygon_filled([(450, 315), (695, 315), (458, 322), (458, 370), (465, 375), (450, 375)], arcade.csscolor.DARK_RED)


def draw_lines2(x, y):
    arcade.draw_rectangle_filled(x, y + 50, 125, 15, arcade.csscolor.BLUE, 0)

draw_lines2.x = SCREEN_WIDTH

def draw_lines(x, y):
    arcade.draw_rectangle_filled(x, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 250, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 250, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 500, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 500, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 750, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 750, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 1000, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_circle_filled(x - 200, y + 400, 70, arcade.csscolor.WHITE_SMOKE, 0)
    arcade.draw_circle_filled(x - 125, y + 380, 50, arcade.csscolor.WHITE_SMOKE, 0)

def draw_road():
    # road
    arcade.draw_rectangle_filled(500, 150, 999, 300, arcade.csscolor.SLATE_GREY)
    arcade.draw_rectangle_filled(500, 300, 999, 15, arcade.csscolor.YELLOW)

def on_draw(delta_time):
    arcade.start_render()
    draw_road()
    for i in range(0, 1250, 250):
        draw_lines2(draw_lines2.x + i, 250)
    if draw_lines2.x == 0:
        draw_lines2.x = SCREEN_WIDTH
    else:
        draw_lines2.x -= 10

    #draw_lines(on_draw.lines_x, 250)
    draw_ferrari()
    on_draw.lines_x += 10
    if on_draw.lines_x == 1200:
        on_draw.lines_x = 0
on_draw.lines_x = 0
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ferrari F-40')
    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()