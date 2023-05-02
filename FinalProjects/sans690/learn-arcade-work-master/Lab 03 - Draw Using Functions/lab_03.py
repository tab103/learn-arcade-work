import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


# Draw face
# Circle
def draw_face(x, y):
    arcade.draw_circle_filled(90 + x, 100 + y, 60, arcade.color.YELLOW)

    # Draw Eyebrow
    arcade.draw_line(50 + x, 120 + y, 70 + x, 110 + y, arcade.color.BLACK, 6)
    arcade.draw_line(110 + x, 110 + y, 130 + x, 120 + y, arcade.color.BLACK, 6)
    # Draw Eyes
    arcade.draw_circle_filled(60 + x, 105 + y, 8, arcade.color.BLACK)
    arcade.draw_circle_filled(120 + x, 105 + y, 8, arcade.color.BLACK)

    # Draw Mouth
    arcade.draw_arc_outline(90 + x, 75 + y, SCREEN_WIDTH - 950, SCREEN_HEIGHT / 40, arcade.color.BLACK, 0, 180, 8)

    # Draw Glasses
    arcade.draw_rectangle_outline(60 + x, 105 + y, SCREEN_WIDTH / 30, SCREEN_HEIGHT / 35, arcade.color.BLACK, 3)
    arcade.draw_rectangle_outline(120 + x, 105 + y, SCREEN_WIDTH / 30,  SCREEN_HEIGHT / 35, arcade.color.BLACK, 3)
    arcade.draw_line(75 + x, 105 + y, 105 + x, 105 + y, arcade.color.BLACK, 3)


def on_draw(delta_time):
    """Draws everything"""
    arcade.start_render()
    draw_face(on_draw.face1_x, 140)
    draw_face(on_draw.face2_x, 531)
    draw_face(on_draw.face3_x, 622)
    draw_face(on_draw.face4_x, 255)

    draw_face(408, on_draw.face5_y)
    draw_face(350, on_draw.face6_y)
    draw_face(500, on_draw.face7_y)
    draw_face(600, on_draw.face8_y)

    # Negative number moves left, positive moves right
    on_draw.face1_x += 13
    on_draw.face2_x -= 10
    on_draw.face3_x -= 6
    on_draw.face4_x -= 8
    # Negative number moves down, positive numbers move up
    on_draw.face5_y -= 13
    on_draw.face6_y += 15
    on_draw.face7_y -= 10
    on_draw.face8_y += 11


# X will start on at:
on_draw.face1_x = 150
on_draw.face2_x = 200
on_draw.face3_x = 300
on_draw.face4_x = 600

# Y will start at:
on_draw.face5_y = 800
on_draw.face6_y = 200
on_draw.face7_y = 205
on_draw.face8_y = 302


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # To run and finish program
    arcade.schedule(on_draw, 1 / 50)
    arcade.run()


# Calls main function to start
main()
