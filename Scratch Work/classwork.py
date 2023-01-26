import arcade   # needed to do anything with the arcade library
import math
arcade.open_window(600, 600, "My Drawing")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
arcade.set_background_color([66, 255, 66])
arcade.start_render()

# between here
# type arcade.draw ... see what tools are in the box

# ugly bus
arcade.draw_polygon_filled([(25,345),(50,400),(350,400),(375,345)],arcade.color.BLUE)
arcade.draw_rectangle_filled(200,320,350,50,arcade.color.GREEN)
arcade.draw_ellipse_filled(100,300,50,50,arcade.color.BLACK)
arcade.draw_ellipse_filled(300,300,50,50,arcade.color.BLACK)

for i in range(360):
    arcade.draw_line(i,300,i,math.sin(math.radians(i)) * 100 + 300, arcade.csscolor.RED)
# and here, be creative!

arcade.finish_render()

print("test string")

arcade.run()