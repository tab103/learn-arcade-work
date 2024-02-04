# import arcade module
import arcade
arcade.open_window(600,600, "Drawing Example")

# Sets background color
# arcade.set_background_color(arcade.csscolor.ALICE_BLUE)
arcade.set_background_color((255, 0, 255))

# Get ready to draw
arcade.start_render()

# Drawing Code HERE
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# End Drawing
arcade.finish_render()

# Keeps window open until someone closes it
arcade.run()
