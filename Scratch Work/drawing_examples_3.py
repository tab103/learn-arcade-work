import arcade   # needed to do anything with the arcade library
import math
import random

arcade.open_window(600, 600, "My Drawing")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()

# between here
# type arcade.draw ... see what tools are in the box
for i in range(1000):
    arcade.draw_line(i/3,200,i/3,math.sin(math.radians(i)) * i/2 + 200, arcade.csscolor.RED)
    arcade.draw_point(i/3+0,math.sin(math.radians(i)) * 100 + 400,arcade.csscolor.BLUE,3)
    arcade.draw_point(i/3+200,math.cos(math.radians(i)) * 100 + 500,arcade.csscolor.GREEN,2)

    for j in range(0,200,20):
        arcade.draw_point(300+50*math.cos(math.radians(i)), j+300+50*math.sin(math.radians(i)),
                          arcade.color.ANTIQUE_BRONZE,2)

    if i % 15 == 0:
        p1 = (i,300 + 200 * math.sin(math.radians(i)))
        p2 = (i + 25,325 + 200 * math.sin(math.radians(i)))
        p3 = (i +50 ,300 + 200 * math.sin(math.radians(i)))
        arcade.draw_triangle_outline(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],arcade.csscolor.YELLOW)
        arcade.draw_text('Nick is one cool guy', p1[0],p1[1],rotation=90)

for x in range (200,500,60):
    for y in range(200,500,60):
        arcade.draw_rectangle_outline(x,y,50,50,arcade.csscolor.WHITE)

# drawing pictures
puppy_texture = arcade.load_texture("puppy.jpg")
scale = 0.2

for i in range(5):
    arcade.draw_scaled_texture_rectangle(random.randint(50,550),random.randint(50,250),puppy_texture,scale,random.randint(0,90))







# and here, be creative!







arcade.finish_render()

print("test string")

arcade.run()