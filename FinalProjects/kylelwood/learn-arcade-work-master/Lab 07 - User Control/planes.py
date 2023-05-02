import arcade

arcade.open_window(600, 600)
arcade.set_background_color(arcade.color.RED)
arcade.start_render()


# draw the plane
arcade.draw_lrtb_rectangle_filled(400, 500, 300, 270, arcade.color.BLACK)
arcade.draw_triangle_filled(350, 270, 400, 301, 400, 270, arcade.color.GRAY)
arcade.draw_triangle_filled(500, 329, 500, 301, 470, 301, arcade.color.BLACK)
arcade.draw_triangle_filled(479, 280, 415, 280, 479, 240, arcade.color.GRAY)

arcade.finish_render()
arcade.run()

