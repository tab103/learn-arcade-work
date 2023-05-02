"""
My Lab 2 Art
"""

# import arcade
import arcade

arcade.open_window(600, 600, "Lab 2 Art")

# set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# ready to draw
arcade.start_render()

# drawing code here
# drawing grass
arcade.draw_rectangle_filled(300, 100, 600, 600, arcade.csscolor.GREEN)

# chimney
arcade.draw_rectangle_filled(290, 415, 20, 60, arcade.csscolor.SADDLE_BROWN)

# draw the house
arcade.draw_rectangle_filled(0, 220, 600, 370, arcade.csscolor.BEIGE)

# house door
arcade.draw_rectangle_filled(120, 95, 60, 120, arcade.csscolor.SIENNA)

# door knob
arcade.draw_circle_filled(140, 100, 5, arcade.csscolor.TAN)

# left Window
arcade.draw_rectangle_filled(45, 300, 80, 80, arcade.csscolor.SIENNA)

# Right Window
arcade.draw_rectangle_filled(250, 300, 80, 80, arcade.csscolor.SIENNA)

# Tree trunk
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree Leaves
arcade.draw_circle_filled(500, 350, 30, arcade.csscolor.LIGHT_GREEN)

# Another tree with Ellipse
arcade.draw_rectangle_filled(550, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(550, 350, 40, 60, arcade.csscolor.FOREST_GREEN)

# draw sun
arcade.draw_circle_filled(600, 600, 100, arcade.csscolor.ORANGE)

# Sun Rays
arcade.draw_line(600, 600, 500, 500, arcade.csscolor.ORANGE, 3)
arcade.draw_line(600, 520, 500, 450, arcade.csscolor.ORANGE, 3)
arcade.draw_line(550, 450, 600, 500, arcade.csscolor.ORANGE, 3)
arcade.draw_line(460, 520, 500, 600, arcade.csscolor.ORANGE, 3)

# rooftop
arcade.draw_triangle_filled(0, 400, 130, 500, 300, 400, arcade.csscolor.SANDY_BROWN)

# Making a pool
arcade.draw_circle_filled(430, 94, 95, arcade.csscolor.GRAY)
arcade.draw_circle_filled(430, 94, 90, arcade.csscolor.LIGHT_BLUE)

# finish drawing

arcade.finish_render()

arcade.run()