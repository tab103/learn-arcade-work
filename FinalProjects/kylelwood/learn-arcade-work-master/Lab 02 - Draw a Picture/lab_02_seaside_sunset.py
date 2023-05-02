import arcade

print("Lab 2")

arcade.open_window(600, 600, "seaside_sunset")

arcade.set_background_color(arcade.color.BURNT_ORANGE)

arcade.start_render()

#draw the sun
arcade.draw_circle_filled(400, 165, 150, arcade.color.SUNRAY)

#draw a sailboat
arcade.draw_lrtb_rectangle_filled(380, 420, 60, 25, arcade.color.BLACK)
arcade.draw_triangle_filled(390, 65, 410, 65, 400, 80, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(399, 401, 70, 50, arcade.color.BLACK)

#draw a house
arcade.draw_circle_filled(42, 222, 15, arcade.color.SMOKE)
arcade.draw_circle_filled(47, 212, 13, arcade.color.SMOKE)
arcade.draw_circle_filled(53, 205, 10, arcade.color.SMOKE)
arcade.draw_circle_filled(57.5, 195, 8, arcade.color.SMOKE)
arcade.draw_lrtb_rectangle_filled(53, 64, 190, 60, arcade.color.SMOKY_BLACK)
arcade.draw_lrtb_rectangle_filled(40, 160, 140, 60, arcade.color.CANDY_APPLE_RED)
arcade.draw_triangle_filled(38, 140, 161, 140, 100, 190, arcade.color.BROWN_NOSE)
arcade.draw_lrtb_rectangle_filled(88, 112, 105, 60, arcade.color.GOLDEN_BROWN)
arcade.draw_lrtb_rectangle_filled(55, 70, 125, 110, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(130, 145, 125, 110, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(55, 70, 117.75, 117, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(62, 62.25, 125, 110, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(130, 145, 117.75, 117, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(137, 137.25, 125, 110, arcade.color.BLACK)


#draw the sea
arcade.draw_lrtb_rectangle_filled(25, 600, 50, 0, arcade.color.HONOLULU_BLUE)

#draw the land
arcade.draw_arc_filled(0, 0, 520, 155, arcade.color.ARMY_GREEN, 0, 90)

arcade.finish_render()
arcade.run()
