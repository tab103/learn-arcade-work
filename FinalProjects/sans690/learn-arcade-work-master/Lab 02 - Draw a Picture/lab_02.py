# Open the "arcade" library
import arcade

# creates a window and opens
# From the "arcade" library. use function called "open_window"
# Window title sets to "Drawing Example"
# Window dimensions set to (width 800 and height 600)
arcade.open_window(800, 600, "Drawing Example")


# sets background color from library
arcade.set_background_color(arcade.color.BLUE)

# ready to draw
arcade.start_render()

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


arcade.finish_render()
# Keep window open
arcade.run()
