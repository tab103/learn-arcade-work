import arcade
def draw_grass(width, height, color):
    arcade.draw_lrtb_rectangle_filled(0, width,
        height / 3, 0, color)