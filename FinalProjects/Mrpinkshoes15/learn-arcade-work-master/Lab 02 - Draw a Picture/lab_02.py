#imports
import arcade
import math


# screen stuff
WIDTH = 1000
HEIGHT = 750
arcade.open_window(WIDTH, HEIGHT, 'Ferrari F-40')
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
x_start = 500
y_start = 375
size = 30
arcade.start_render()

red = arcade.color.RED
black = arcade.csscolor.BLACK
slate = arcade.csscolor.SLATE_GREY
yellow = arcade.csscolor.YELLOW
gray = arcade.csscolor.SLATE_GREY
dr = arcade.csscolor.DARK_RED
silver = arcade.csscolor.SILVER

#front hood
arcade.draw_arc_filled(524, 300, 530, 196, red, 10, 160)
# road
arcade.draw_rectangle_filled(500, 150, 999, 300, slate)
arcade.draw_rectangle_filled(500, 300, 999, 15, yellow)

#windows
arcade.draw_arc_filled(585, 325, 400, 230, gray, 40, 180)
arcade.draw_polygon_filled([(720, 410), (770, 388), (700, 388)], gray)
#rear/mid car body
arcade.draw_polygon_filled([(780, 390), (430,375), (430, 305), (760, 305), (780, 310) ], red)
#rear wing
arcade.draw_polygon_filled([(838, 327), (780, 310), (780, 390), (795, 425), (838, 425)], red)
#front spliter
arcade.draw_polygon_filled([(430, 330), (275, 325), (270, 305), (430, 305)], red)
#front fender
arcade.draw_polygon_filled([(418,390), (450,375), (430, 330), (275, 325), (280, 338)], red)
# A and B pillars
arcade.draw_polygon_filled([(430, 375), (440, 375), (520, 429), (620, 429), (670, 396), (660, 385), (740, 388), (630, 437), (520, 437)], red)
#wheel arches
arcade.draw_arc_filled(385, 305, 105, 140, dr, 0, 180)
arcade.draw_arc_filled(740, 305, 105, 140, dr, 8.30, 180)
# wheels
arcade.draw_ellipse_filled(385, 326, 90, 90, black, 0,)
arcade.draw_ellipse_filled(740, 326, 92, 92, black, 0)
arcade.draw_ellipse_filled(385, 326, 70, 70, silver, 0,)
arcade.draw_ellipse_filled(740, 326, 72, 72, silver, 0)
# side details
arcade.draw_polygon_filled([(510, 372), (640, 378), (637, 350)], dr)
arcade.draw_polygon_filled([(600, 327), (665, 338), (663, 318)], dr)
arcade.draw_polygon_filled([(450, 315), (695, 315), (458, 322), (458, 370), (465, 375), (450, 375)],
                           arcade.csscolor.BLACK, 0,)



arcade.finish_render()
arcade.run()