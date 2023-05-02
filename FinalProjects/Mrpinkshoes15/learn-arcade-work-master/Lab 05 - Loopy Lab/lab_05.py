import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    pass


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    pass


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    pass


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    pass


def draw_section_6():
    pass


def draw_section_7():
    pass


def draw_section_8():
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    def draw_section_1(center_x, center_y):
        arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.WHITE)

    for x in range(5, 300, 10):
        for y in range(5, 300, 10):
             draw_section_1(x, y)


    def draw_section_2():

        for x in range(315, 600, 20):
            for y in range(5, 300, 10):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.BLACK)
        for x in range(305, 600, 20):
            for y in range(5, 300, 10):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.WHITE)
    draw_section_2()

    def draw_section_3():
        for x in range(605, 900, 10):
            for y in range(15, 300, 20):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.BLACK)
        for x in range(605, 900, 10):
            for y in range(5, 300, 20):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.WHITE)
    draw_section_3()


    def draw_section_4():
        for x in range(905, 1200, 20):
            for y in range(15, 300, 20):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.BLACK)
    draw_section_4()
    def draw_section_5(center_x, center_y):
        arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)

    for x in range( 295, 0, -10):
        for y in range(x + 295, 300, -10):
            draw_section_5(x, y)

    def draw_section_6(center_x, center_y):
        arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)

    for x in range( 595, 300, 10):
        for y in range(x + 295, 300, -10):
            draw_section_6(x, y)

    def draw_section_7(center_x, center_y):
        arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)

    for x in range(605, 900, 10):
        for y in range(x - 300, 800, 10):
             draw_section_7(x, y)


    def draw_section_8(center_x, center_y):
        arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)

    for x in range( 295, 0, -10):
        for y in range(x + 295, 300, -10):
            draw_section_8(x, y)

    arcade.finish_render()

    arcade.run()


main()