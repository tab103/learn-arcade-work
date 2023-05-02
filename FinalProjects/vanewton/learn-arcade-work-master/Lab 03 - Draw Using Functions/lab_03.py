import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.DARK_BLUE)
arcade.start_render()
def draw_pizza(x,y):
    #draw the crust
    arcade.draw_rectangle_filled(x,y,500,50, (115,58,58))
    #draw the base with cheese
    arcade.draw_triangle_filled(x-250,y-25,x+250,y-25,x,y-500, (247,208,52))
    #draw the pepperoni
    arcade.draw_circle_filled(x-100,y-125,50, (178,13,46))
    arcade.draw_circle_filled(x+100,y-125,50, (178,13,46))
    arcade.draw_circle_filled(x,y-215,50, (178,13,46))
    arcade.draw_circle_filled(x,y-350,50, (178,13,46))


def on_draw(delta_time):
    arcade.start_render()
    draw_pizza(on_draw.pizza1_x,495)

    on_draw.pizza1_x += 10

on_draw.pizza1_x=-300
arcade.schedule(on_draw, 1/60)

#  Finish and run
arcade.run()