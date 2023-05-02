import arcade
import math
arcade.open_window(1000, 600, "fun ideas")
arcade.set_background_color(arcade.color. WHITE)
arcade.start_render()

#sun reflection function
def sun_reflect(num_lines):
    startx=550 
    starty=290
    endx= 650
    endy=290

    for x in range (0, num_lines):
         startx-=10
         endx+=10
         starty-=20
         endy-=20
         arcade.draw_line(startx,starty, endx, endy, color=arcade.color.RED_ORANGE )
sun_reflect(6)


for j in range(0, 360, 20):
    arcade.draw_triangle_filled(140+math.cos(math.radians(j)), 30+math.sin(math.radians(j)), 44, 200, 45, 100, arcade.color. BLUE, -j)

    # for j in range(0, 360, 20):
    #     arcade.draw_ellipse_filled(x + math.cos(math.radians(j)) * flower_size,
    #                                y + math.sin(math.radians(j)) * flower_size,
    #                                flower_size, flower_size / 3, arcade.csscolor.YELLOW, -j)






arcade.finish_render()
arcade.run()