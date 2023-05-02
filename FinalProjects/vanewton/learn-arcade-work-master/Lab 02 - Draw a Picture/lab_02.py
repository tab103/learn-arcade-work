import arcade
import math
import random
arcade.open_window(600,600, "My Drawing")
arcade.set_background_color((0,225,255))
arcade.start_render()

#draw the crust
arcade.draw_rectangle_filled(300,500,500,50, (115,58,58))

#draw the base with cheese
arcade.draw_triangle_filled(50,475,550,475,300,25, (247,208,52))

#draw the pepperoni
arcade.draw_circle_filled(200,400,50, (178,13,46))
arcade.draw_circle_filled(400,400,50, (178,13,46))
arcade.draw_circle_filled(300,300,50, (178,13,46))
arcade.draw_circle_filled(300,170,50, (178,13,46))


#finish and render
arcade.finish_render()
arcade.run()