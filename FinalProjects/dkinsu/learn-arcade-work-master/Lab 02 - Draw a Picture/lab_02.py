# using arcade library
import arcade

# creating a 600x600 pixel window for the drawing and setting background color
arcade.open_window(600, 600, "house drawing")
arcade.set_background_color((100, 156, 245))
# beginning render
arcade.start_render()

# drawing grass
arcade.draw_rectangle_filled(300, 100, 600, 200, (3, 173, 15))

# drawing main body of house
arcade.draw_rectangle_filled(300, 300, 300, 250, (224, 94, 67))
# adding a door
arcade.draw_rectangle_outline(300, 260, 130, 160, (255, 255, 255))
arcade.draw_rectangle_filled(300, 260, 128, 158, (127, 127, 127))
arcade.draw_circle_filled(350, 240, 5, (0, 0, 0), 0)
# adding a roof
arcade.draw_triangle_filled(120, 425, 480, 425, 300, 570, (30, 30, 30))
# drawing a "diamond" window
arcade.draw_polygon_filled([(280, 480), (300, 460), (320, 480), (300, 500)], (255, 255, 255))
arcade.draw_polygon_filled([(282, 480), (300, 462), (318, 480), (300, 498)], (0, 0, 0))
arcade.draw_line(280, 480, 320, 480, (255, 255, 255), 1)
arcade.draw_line(300, 460, 300, 500, (255, 255, 255), 1)

# drawing 2 clouds
arcade.draw_ellipse_filled(80, 540, 120, 45, (240, 240, 240))
arcade.draw_ellipse_filled(490, 550, 120, 45, (240, 240, 240))

# ending render, run keeps render open until manually closed
arcade.finish_render()
arcade.run()
