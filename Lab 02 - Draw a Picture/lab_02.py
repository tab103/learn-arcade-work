# import arcade module
import arcade
arcade.open_window(600,600, "Drawing Example")

# Sets background color
# arcade.set_background_color(arcade.csscolor.ALICE_BLUE)
arcade.set_background_color((0, 0, 0))

# Starts drawing
arcade.start_render()

# Drawing Code
# Ground
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (84, 58, 51))

# Trees
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(600, 320, 20, 60, arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(450, 320, 20, 60, arcade.csscolor.SIENNA)

# Leaves on Trees
arcade.draw_circle_filled(300, 380, 40, arcade.csscolor.DARK_OLIVE_GREEN)

arcade.draw_circle_filled(600, 380, 40, (43, 66, 29))

arcade.draw_circle_filled(450, 380, 40, (26, 51, 24))

arcade.draw_circle_filled(100, 380, 40, (32, 82, 29))

# Moon
arcade.draw_circle_filled(400, 500, 60, arcade.csscolor.WHITE)
# To make it a Crescent
arcade.draw_circle_filled(420, 500, 60, arcade.csscolor.BLACK)

# Apples on tree at 450 x
arcade.draw_circle_filled(450, 380, 5, (171, 57, 46))

arcade.draw_circle_filled(425, 360, 5, (171, 57, 46))

arcade.draw_circle_filled(480, 360, 5, (171, 57, 46))

arcade.draw_circle_filled(470, 390, 5, (171, 57, 46))

# End Drawing
arcade.finish_render()

# Keeps window open until someone closes it
arcade.run()