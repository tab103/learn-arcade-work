import arcade
# minecraft iron block
cube_pic = arcade.load_texture('iron_block.jpg')
# minecraft zombie
green_pic = arcade.load_texture('green.jpg')
# minecraft ender dragon
dragon_pic = arcade.load_texture('dragon.jpg')
# minecraft wither
fiend_pic = arcade.load_texture('fiend.png')
def cube_draw():
    arcade.open_window(600, 600, 'CUBE')
    arcade.start_render()
    arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, cube_pic)
    arcade.finish_render()
    arcade.run()

def green_draw():
    arcade.open_window(600, 600, 'Green Warrior')
    arcade.start_render()
    arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, green_pic)
    arcade.finish_render()
    arcade.run()

def dragon_draw():
    arcade.open_window(600, 600, 'Guardian Dragon')
    arcade.start_render()
    arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, dragon_pic)
    arcade.finish_render()
    arcade.run()

def fiend_draw():
    arcade.open_window(600, 600, 'Underworld Fiend')
    arcade.start_render()
    arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, fiend_pic)
    arcade.finish_render()
    arcade.run()

