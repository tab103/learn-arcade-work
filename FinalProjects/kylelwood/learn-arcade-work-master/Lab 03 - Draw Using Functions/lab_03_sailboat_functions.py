import arcade


def draw_sun():
    # draw the sun
    arcade.draw_circle_filled(400, 165, 150, arcade.color.SUNRAY)


def draw_sailboat(x, y):
    # draw a sailboat
    arcade.draw_lrtb_rectangle_filled(380 + x, 420 + x, 60 + y, 50 + y, arcade.color.BLACK)
    arcade.draw_triangle_filled(390 + x, 65 + y, 410 + x, 65 + y, 400 + x, 80 + y, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(399 + x, 401 + x, 70 + y, 50 + y, arcade.color.BLACK)


def draw_house():
    # draw a house
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


def draw_sea():
    # draw the sea
    arcade.draw_lrtb_rectangle_filled(25, 600, 50, 0, arcade.color.HONOLULU_BLUE)


def draw_land():
    # draw the land
    arcade.draw_arc_filled(0, 0, 520, 155, arcade.color.ARMY_GREEN, 0, 90)


def on_draw(time):
    arcade.start_render()
    draw_sun()
    draw_house()
    draw_sea()
    draw_land()
    draw_sailboat(on_draw.sailboat1_x, 1)


# add -1 value to make sailboat move left
on_draw.sailboat1_x -= 3


if on_draw.sailboat1_x < -200:
    on_draw.sailboat1_x = 200


arcade.finish_render()


# sailboat starting point
on_draw.draw_sailboat = 200


def main():
    arcade.open_window(600, 600, "seaside_sunset_lab3")
    arcade.set_background_color(arcade.color.BURNT_ORANGE)


# call on_draw function every 1/20 second
arcade.schedule(on_draw, 1/20)
arcade.run()

main()
