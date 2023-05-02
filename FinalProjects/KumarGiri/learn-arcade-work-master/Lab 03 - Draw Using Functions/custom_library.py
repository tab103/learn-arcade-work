import arcade
import math

# to draw a single cloud using ellipse 
def cloud_ovals(x_center, y_center):
    arcade.draw_ellipse_filled(x_center, y_center, width=50, height=30, color=arcade.color.ASH_GREY)

# to draw a sigle cloud
def cloud(x_center, y_center):
     cloud_ovals(x_center, y_center)
     cloud_ovals(x_center+25, y_center)
     cloud_ovals(x_center+25, y_center+10)

# to call all the cloud clusters
def cloud_clusters(x):
    cloud(755-x/1.5, 500)
    cloud(650-x, 450)
    cloud(770-x/2, 420)


# to draw a brach and leaves
def leafs(x_center, y_center, tangle):
    arcade.draw_line(647, 600, 625, 450, color=arcade.color.WARM_BLACK)
    arcade.draw_ellipse_filled(x_center, y_center, 50, 10, color=arcade.color.WARM_BLACK, tilt_angle=tangle)

# drawing leaves around the branch
def individual_leaves():
    x_center= 650
    y_center= 475
    for x in range (1,8):
        x_center +=3
        y_center +=18
        leafs(x_center, y_center, 30)
    x_center= 612
    y_center= 475
    for x in range (1,8):
        x_center +=2
        y_center +=18
        leafs(x_center, y_center, 145)


# to draw the Sun and its rays
def sun(x, y, radius):
    """larger rays"""
    for j in range(0,360, 40):
        arcade.draw_line(x+50*math.sin(math.radians(j)), y+50*math.cos(math.radians(j)), x+30*math.sin(math.radians(j)), y+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)

        """smaller rays"""
        for j in range(20,380, 40):
            arcade.draw_line(x+45*math.sin(math.radians(j)), y+45*math.cos(math.radians(j)), x+30*math.sin(math.radians(j)), y+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)
    arcade.draw_circle_filled(x, y, radius, arcade.color.SUNGLOW)
    
    """drawing a point x, y for reference"""
    arcade.draw_point(x, y, arcade.color.RED, 5)



