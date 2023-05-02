"""
Array Backed Grid

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        self.row_counter = []
        self.ir = 0
        self.selected = 0
        self.continuous_count = 0
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.row_counter.append([])
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.row_counter[row].append(0)
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")



        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist


        # is valid
        self.grid[row][column] = 1 - self.grid[row][column]

        # row-1, column
        if 0 <= row - 1 < ROW_COUNT and 0 <= column < COLUMN_COUNT: # check for valid
            self.grid[row - 1][column] = 1 - self.grid[row - 1][column]
        #row +1
        if 0 <= row + 1 < ROW_COUNT and 0 <= column < COLUMN_COUNT:  # check for valid
            self.grid[row + 1][column] = 1 - self.grid[row + 1][column]
        #column + 1
        if 0 <= row < ROW_COUNT and 0 <= column - 1 < COLUMN_COUNT:  # check for valid
            self.grid[row][column - 1] = 1 - self.grid[row][column - 1]
        #column - 1
        if 0 <= row < ROW_COUNT and 0 <= column + 1 < COLUMN_COUNT:  # check for valid
            self.grid[row][column + 1] = 1 - self.grid[row][column + 1]

        self.selected = 0
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if self.grid[i][j] == 1:
                    self.selected = self.selected + 1
        print("Total of", self.selected, "cells selected")

        self.selected = 0
        for i in range(ROW_COUNT):
            row_counter = 0
            for j in range(COLUMN_COUNT):
                if self.grid[i] == 1:
                    self.selected = self.selected + 1
                    row_counter = self.row_count[row][column]
        print("Row has", self.selected, "cells selected")

        self.selected = 0
        for i in range(COLUMN_COUNT):
            for j in range(ROW_COUNT):
                if self.grid[i][j] == 1:
                    self.selected = self.selected + 1
        print("column", self.selected, "cells selected")

        if self.grid ==1:
            self.continuous_count += 1
        else:
            if self.continuous_count ==0:
                self.continuous_count <= 0




















def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()