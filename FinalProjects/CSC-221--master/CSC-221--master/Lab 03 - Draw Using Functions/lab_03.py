import arcade

ray_x = 0
ray_y = 600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_sun(x, y):
    """draw sun"""
    arcade.draw_circle_filled(0, 600, 100, arcade.csscolor.YELLOW)
def draw_tree(x, y):
    """draw tree"""
    arcade.draw_rectangle_filled(550 + x , 230 + y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(550 + x, 250 + y, 30, arcade.csscolor.WHITE)
def draw_panda(x, y):
    """draw a panda"""
    arcade.draw_circle_filled(360 + x, 180 + y, 90, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(360 + x, 200 + y, 90, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(350 + x, 200 + y, 90, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(320 + x, 180 + y, 90, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(260 + x, 295 + y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(300 + x, 230 + y, 70, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(315 + x, 300 + y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(255 + x, 240 + y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(300 + x, 240 + y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(255 + x, 240 + y, 10, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300 + x, 240 + y, 10, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(260 + x, 235 + y, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(305 + x, 235 + y, 5, arcade.csscolor.BLACK)
    arcade.draw_triangle_filled(255 + x, 200 + y, 285 + x, 200 + y, 270 + x, 220 + y, arcade.csscolor.BLACK)
    arcade.draw_arc_outline(300 + x, 220 + y, 100, 100, arcade.csscolor.BLACK, 180, 270, 5, 45)
    arcade.draw_ellipse_filled(310 + x, 100 + y, 30, 80, arcade.color.AIR_SUPERIORITY_BLUE, 180)
    arcade.draw_circle_filled(320 + x, 105 + y, 15, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(295 + x, 105 + y, 15, arcade.csscolor.BLACK)
def draw_igloo(x, y):
    """draw an igloo"""
    arcade.draw_circle_filled(60 + x, 250 + y, 100, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(50 + x, 150 + y, 200, 60, arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.draw_line(60 + x, 350 + y, 60 + x, 180 + y, arcade.color.AIR_SUPERIORITY_BLUE, 3)
    arcade.draw_line(-50 + x, 190 + y, 200 + x, 190 + y, arcade.color.AIR_SUPERIORITY_BLUE, 3)
    arcade.draw_line(-40 + x, 240 + y, 160 + x, 240 + y, arcade.color.AIR_SUPERIORITY_BLUE, 3)
    arcade.draw_line(-30 + x, 300 + y, 148 + x, 300 + y, arcade.color.AIR_SUPERIORITY_BLUE, 3)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.schedule(on_draw,1/60)
    arcade.run()

def on_draw(z):
    arcade.start_render()
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
    """draw everything"""
    draw_sun(0, 0)
    draw_tree(50, 0)
    draw_tree(90, 0)
    draw_tree(130, 0)
    draw_tree(210, 0)
    draw_igloo(40, 0)
    global ray_x, ray_y
    draw_panda(0, 0)
    ray_x += 1
    ray_y -= 1
    for i in range(0, 600, 50):
        arcade.draw_line(ray_x + i, ray_y, ray_x + 30 + i, ray_y - 60, arcade.csscolor.YELLOW,3)

    # Finish and run
    arcade.finish_render()

main()
