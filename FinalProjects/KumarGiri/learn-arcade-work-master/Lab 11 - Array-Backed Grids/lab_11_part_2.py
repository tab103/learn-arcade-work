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
    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
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

    # function for changing color
    def flip_cell(self, row, column):
        if 0 <= row < ROW_COUNT and 0 <= column < COLUMN_COUNT:
            self.grid[row][column] = 1 - self.grid[row][column]

    def on_mouse_press(self, x, y, button, modifiers):

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        coordinates = []
        for a in range(ROW_COUNT):
            for b in range(COLUMN_COUNT):
                coordinates.append([a, b])

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
            self.flip_cell(row, column)
            self.flip_cell(row + 1, column)
            self.flip_cell(row - 1, column)
            self.flip_cell(row, column - 1)
            self.flip_cell(row, column + 1)

            # part 2 codes

        no_of_cells_selected = 0
        no_of_cells_in_row = []

        for row in range(ROW_COUNT):
            continuous_count = 0
            colored_cells = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    no_of_cells_selected += 1
                    continuous_count += 1
                    colored_cells += 1
            no_of_cells_in_row.append(colored_cells)
            if continuous_count > 2:
                print(f'There are {continuous_count} continuous cells on {row + 1} row')
        print(f'There are a total of {no_of_cells_selected} cells selected')
        for row in range(ROW_COUNT):
            print(f'The row {row + 1} has {no_of_cells_in_row[row]} cells selected')

        # column cells
        no_of_cells_in_column = []
        for column in range(COLUMN_COUNT):
            columns = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    columns += 1
            no_of_cells_in_column.append(columns)
        for column in range(COLUMN_COUNT):
            print(f'The column {column + 1} has {no_of_cells_in_column[column]} cells selected')


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
