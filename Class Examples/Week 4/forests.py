import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_tree(x, y, scale):
    # draw trunk
    trunk_list = [(x + scale+10,y),(x+20+scale, y),(x+20+scale,y+40+scale * 4),(x+scale+10,y + 30 + scale * 4)]
    canopy_list = [(x + 5,y + 30 + scale * 4),(x + 5 + 30 + scale, y + 30 + scale * 4),(x + 5 + (30+scale)/2,y+80+scale * 8)]
    arcade.draw_polygon_filled(trunk_list,arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(canopy_list, arcade.csscolor.GREEN)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Random Forests")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()

# Draw the ground
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_GREEN)

for s in range(1,20):
    draw_tree(s*40,50,s)

#  Finish and run
arcade.finish_render()
arcade.run()