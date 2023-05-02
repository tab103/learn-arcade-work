import arcade
def draw_ground(x, y):
    #drawing green rectangle for grass and dark gray rectangle on top for street
    arcade.draw_rectangle_filled(300 + x, 100 + y, 600, 200, (3, 173, 15))
    arcade.draw_rectangle_filled(300 + x, 50 + y, 600, 150, (46, 49, 54))
def draw_cloud(x, y):
    #drawing a cloud, made with four ellipses
    arcade.draw_ellipse_filled(x - 30, y, 120, 45, (240, 240, 240))
    arcade.draw_ellipse_filled(x, 15 + y, 120, 45, (240, 240, 240))
    arcade.draw_ellipse_filled(30 + x, y, 120, 45, (240, 240, 240))
    arcade.draw_ellipse_filled(x, y - 15, 120, 45, (240, 240, 240))
def draw_house(x, y):
    # drawing main body of house
    arcade.draw_rectangle_filled(300 + x, 300 + y, 300, 250, (224, 94, 67))
    # adding a door
    arcade.draw_rectangle_outline(300 + x, 260 + y, 130, 160, (255, 255, 255))
    arcade.draw_rectangle_filled(300 + x, 260 + y, 128, 158, (127, 127, 127))
    arcade.draw_circle_filled(350 + x, 240 + y, 5, (0, 0, 0), 0)
    # adding a roof
    arcade.draw_triangle_filled(120 + x, 425 + y, 480, 425, 300, 570, (30, 30, 30))
    # drawing a "diamond" window
    arcade.draw_polygon_filled([(280 + x, 480 + y), (300 + x, 460 + y), (320 + x, 480 + y), (300 + x, 500 + y)], (255, 255, 255))
    arcade.draw_polygon_filled([(282 + x, 480 + y), (300 + x, 462 + y), (318 + x, 480 + y), (300 + x, 498 + y)], (0, 0, 0))
    arcade.draw_line(280 + x, 480 + y, 320, 480, (255, 255, 255), 1)
    arcade.draw_line(300 + x, 460 + y, 300 + x, 500 + y, (255, 255, 255), 1)
def main():
    arcade.open_window(600, 600, "house drawing")
    arcade.set_background_color((100, 156, 245))
    # beginning render
    arcade.start_render()
    # ending render, run keeps render open until manually closed
    draw_ground(0,0)
    draw_cloud(100, 500)
    draw_cloud(460, 450)
    draw_cloud(500, 550)
    draw_house(0, 0)
    arcade.finish_render()
    arcade.run()

main()