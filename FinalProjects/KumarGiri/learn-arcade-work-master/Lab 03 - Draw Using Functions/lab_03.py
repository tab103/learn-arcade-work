import arcade

HEIGHT = 600
WIDTH = 800

# function for drawing hills using ellipses
def hills(x_center, y_center, length, height, startangle, endangle, hill_color):
    arcade.draw_arc_filled(x_center, y_center, length, height, color=hill_color, start_angle=startangle, end_angle=endangle)

# function for drawing birds using arcs 
def bird(x, ystart):
    arcade.draw_arc_outline(x, ystart, 15, 15, arcade.color.BLACK, 0, 155, 4)
    arcade.draw_arc_outline(x+14, ystart, 15, 15, arcade.color.BLACK, 35, 180, 4)


# draw everything
def on_draw(deltatime):
    arcade.start_render()
    # importing a custom library 
    import custom_library as cl

    cl.sun(on_draw.x/2+200, 530-on_draw.x/3, 30)
   
    cl.cloud_clusters(on_draw.x)
 
    bird(on_draw.x/3+230, on_draw.x/8+400)
    bird(on_draw.x/2+175, on_draw.x/10+400)

    hills(0, 0, 700, 400, 0, 90, arcade.color.ARMY_GREEN)
    hills(800, 0, 600, 500, 90, 180, arcade.color.DARK_GREEN )
    hills(500, 0, 400, 300, 0, 180, arcade.color.SAP_GREEN)

    cl.leafs(628, 450,90)
    cl.leafs(650, 475, 45)
    cl.leafs(612, 475, 135)
    cl.individual_leaves()

    on_draw.x += 1

    arcade.finish_render()
on_draw.x = 0

# main function
def main():
    arcade.open_window(WIDTH, HEIGHT, "Draw Using functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(on_draw, 1/30)
    arcade.run()

# call main function    
main()