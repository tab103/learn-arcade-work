import arcade
import math

# draw "Ship at sea" background
def draw():
        arcade.draw_lrtb_rectangle_filled(0, 1000, 600, 300, color=arcade.color_from_hex_string(code='#8fc2f1'))

        # blue water background
        arcade.draw_rectangle_filled(center_x=500, center_y=225, height=150, width=1000, color=arcade.color.BLUE_GREEN)

        # draw ground
        arcade.draw_rectangle_filled(center_x=500, center_y=75, height= 150, width=1000, color=arcade.color_from_hex_string(code='#235810'))

        # draw the ship body
        x1= 150
        y1= 320
        x2= 450
        y2= 320
        arcade.draw_polygon_filled([[x1, y1], [x2, y2], [x2-35, y2-70], [x1+35, y1-70]], color=arcade.color.BROWN)
        arcade.draw_polygon_filled([[x1+30, y1+25], [x2-40, y2+25], [x2-30, y2], [x1+30, y1]], arcade.color.TAN)

        # draw four circles on the ship
        arcade.draw_circle_filled(220, 280, 15, arcade.color.SAPPHIRE_BLUE)
        arcade.draw_circle_filled(270, 280, 15, arcade.color.SAPPHIRE_BLUE)
        arcade.draw_circle_filled(320, 280, 15, arcade.color.SAPPHIRE_BLUE)
        arcade.draw_circle_filled(370, 280, 15, arcade.color.SAPPHIRE_BLUE)

        # draw three steam exhausts
        arcade.draw_lrtb_rectangle_filled(370, 385, 370, 345, color=arcade.color.OLD_SILVER)
        arcade.draw_lrtb_rectangle_filled(300, 315, 370, 345, color=arcade.color.OLD_SILVER)
        arcade.draw_lrtb_rectangle_filled(230, 245, 370, 345, color=arcade.color.OLD_SILVER)

        # draw smoke
        arcade.draw_ellipse_filled(375, 390, 10,8, arcade.color.COOL_GREY, 18)
        arcade.draw_ellipse_filled(290, 390, 15,10, arcade.color.COOL_GREY, 15)

        # draw 3 layers of sunlight shadings
        arcade.draw_arc_filled(center_x=600, center_y=300, width= 300, height=300, color=arcade.color_from_hex_string(code='#d58cc7'),start_angle=0, end_angle=180, tilt_angle=0)
        arcade.draw_arc_filled(center_x=600, center_y=300, width= 200, height=200, color=arcade.color_from_hex_string(code='#fc97a4'),start_angle=0, end_angle=180, tilt_angle=0)
        arcade.draw_arc_filled(center_x=600, center_y=300, width= 150, height=150, color=arcade.color_from_hex_string(code='#f6aa93'),start_angle=0, end_angle=180, tilt_angle=0)

        # draw the setting Sun
        arcade.draw_arc_filled(center_x=600, center_y=300, width= 100, height=100, color=arcade.color_from_hex_string(code='#f1c581'),start_angle=0, end_angle=180, tilt_angle=0)

        # draw a cloud
        arcade.draw_ellipse_filled( 200, 540, width=100, height=60, color=arcade.color.ASH_GREY)
        arcade.draw_ellipse_filled( 240, 540, width=100, height=60, color=arcade.color.ASH_GREY)
        arcade.draw_ellipse_filled( 240,565, width=100, height=60, tilt_angle=20, color=arcade.color.ASH_GREY)

# draw the sun
def sun(x, y, radius= 20):
    """larger rays"""
    for j in range(0,360, 40):
        arcade.draw_line(x+50*math.sin(math.radians(j)), y+50*math.cos(math.radians(j)), x+30*math.sin(math.radians(j)), y+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)

        """smaller rays"""
        for j in range(20,380, 40):
            arcade.draw_line(x+45*math.sin(math.radians(j)), y+45*math.cos(math.radians(j)), x+30*math.sin(math.radians(j)), y+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)
    arcade.draw_circle_filled(x, y, radius, arcade.color.SUNGLOW)


# draw the moon
def moon(x, y, radius):
     arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)
     arcade.draw_triangle_filled(x, y+radius, x+radius, y, x+10+radius, y+10+radius, arcade.color.WHITE)
     arcade.draw_triangle_filled(x, y-radius, x+10+radius, y-(10+radius), x+radius, y, arcade.color.WHITE)
     arcade.draw_triangle_filled(x, y+radius, x-(10+radius), y+(10+radius), x-radius, y, arcade.color.WHITE)
     arcade.draw_triangle_filled(x-radius, y, x-(10+radius), y-(10+radius), x, y-radius, arcade.color.WHITE)