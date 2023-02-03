"""An approximation of using Newton's Second Law to simulate projectile motion"""
import arcade
import sys
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CANNON_SCALE = 0.2
GRAVITY = 9.81

cannon_texture = arcade.load_texture("cannon.png")

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.GREEN)

def draw_cannon(x, y):
    arcade.draw_scaled_texture_rectangle(x, y, cannon_texture, CANNON_SCALE, on_draw.angle)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    #draw_grass()
    draw_cannon(100,100) # move as needed

    # check to see if in flight
    if on_draw.inflight == True:
        # Use Newton's Second Law to Calculate Position
        on_draw.x = on_draw.x + on_draw.xforce * on_draw.time
        on_draw.y = on_draw.y + on_draw.yforce * on_draw.time + 0.5 * -GRAVITY * math.pow(on_draw.time, 2)
        print(on_draw.x, on_draw.y)
        if on_draw.x >= SCREEN_WIDTH or on_draw.y <= 0:
            sys.exit()
        arcade.draw_circle_filled(on_draw.x, on_draw.y, 15, arcade.csscolor.BLACK)
        on_draw.time += 0.02
    arcade.finish_render()

on_draw.inflight = False
on_draw.x = 100 # adjust
on_draw.y = 100
on_draw.angle = 45
on_draw.force = 10
on_draw.xforce = on_draw.force * math.cos(math.radians(on_draw.angle))
on_draw.yforce = on_draw.force * math.sin(math.radians(on_draw.angle))
on_draw.time = 0

def main(args):
    while True:
        on_draw.angle = float(input("Enter firing angle: "))
        on_draw.force = float(input("Enter firing force: "))
        on_draw.xforce = on_draw.force * math.cos(math.radians(on_draw.angle))
        on_draw.yforce = on_draw.force * math.sin(math.radians(on_draw.angle))
        on_draw.inflight = True

        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        # Call on_draw every 60th of a second.
        arcade.schedule(on_draw, 1/60)
        arcade.run()

# Call the main function to get the program started.
main(sys.argv[1:])