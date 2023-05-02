""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
    arcade.set_background_color(0,255,255)

    #create the pizza
        self.pizza = Pizza(50,50,15,arcade.color,0,255,255)


class Pizza:
    def on_draw(self):
        arcade.start_render()
        self.draw_pizza(300,300)
        self.on_draw()


    def draw_pizza(x, y):
        # draw the crust
        arcade.draw_rectangle_filled(x, y, 500, 50, (115, 58, 58))
        # draw the base with cheese
        arcade.draw_triangle_filled(x - 250, y - 25, x + 250, y - 25, x, y - 500, (247, 208, 52))
        # draw the pepperoni
        arcade.draw_circle_filled(x - 100, y - 125, 50, (178, 13, 46))
        arcade.draw_circle_filled(x + 100, y - 125, 50, (178, 13, 46))
        arcade.draw_circle_filled(x, y - 215, 50, (178, 13, 46))
        arcade.draw_circle_filled(x, y - 350, 50, (178, 13, 46))

        self.pizza.draw = Pizza(50,51,50)




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()