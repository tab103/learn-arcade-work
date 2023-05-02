""" Sprite Sample Program """

"""How to play the game:
1. use the arrow keys to change directions or the mouse
2. to go faster, press the keys again
3. collect coins to add points to your score
4. avoid the rocks, collision with them will decrease your score
"""

import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_TANK = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_ROCK = 0.3
COIN_COUNT = 5
ROCK_COUNT = 20
TANK_SPEED = 1
ROCK_SPEED = 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# the player avatar is a tank
class Tank(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x=0
        self.center_y=0
        self.change_x = TANK_SPEED
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

# the coin class
class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0

    def update(self):
        self.center_y -= 1
        self.center_x += 1
        if self.center_x > SCREEN_WIDTH:
            self.center_x= 0
            self.center_y=random.randrange(SCREEN_HEIGHT)
        if self.center_y <0:
            self.center_y =SCREEN_HEIGHT
            self.center_x = random.randrange(SCREEN_WIDTH)

# the obstacles
class Rock(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x=0
        self.center_y=0
        self.angle=0

    def update(self):
        self.center_x +=ROCK_SPEED
        self.angle +=1
        self.center_y += math.sin(math.radians(self.angle))
        if self.center_x>SCREEN_WIDTH:
            self.center_x = 0
            self.center_y = random.randrange(SCREEN_HEIGHT)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        arcade.set_background_color(arcade.color.POWDER_BLUE)
        self.coin_sound = arcade.load_sound("clicks.wav")
        self.rock_sound = arcade.load_sound("wall.mp3")

        self.tank_sprite_list= None
        self.coin_sprite_list= None
        self.rock_sprite_list= None
        self.score = 0
        self.sound= 0
        self.rock_touched=0

        self._mouse_visible = False

    def setup(self):
        self.coin_sprite_list = arcade.SpriteList()
        self.tank_sprite_list = arcade.SpriteList()
        self.rock_sprite_list = arcade.SpriteList()

        self.tank_sprite = Tank("tank.png", SPRITE_SCALING_TANK)
        self.tank_sprite.center_x = 50
        self.tank_sprite.center_y = 50
        self.tank_sprite_list.append(self.tank_sprite)


        # draw coins
        for i in range(COIN_COUNT):
            self.coin_sprite = Coin("coin.png", SPRITE_SCALING_COIN)
            self.coin_sprite.center_x= random.randrange(SCREEN_WIDTH)
            self.coin_sprite.center_y= random.randrange(SCREEN_HEIGHT)
            self.coin_sprite_list.append(self.coin_sprite)

        for i in range(ROCK_COUNT):
            rock_sprite = Rock("stone.png", SPRITE_SCALING_ROCK)
            rock_sprite.center_x = random.randrange(SCREEN_WIDTH)
            rock_sprite.center_y= random.randrange(SCREEN_HEIGHT)
            self.rock_sprite_list.append(rock_sprite)


    def on_draw(self):
        arcade.start_render()
        self.coin_sprite_list.draw()
        self.rock_sprite_list.draw()
        self.tank_sprite_list.draw()

        output= f"score: {self.score}"

        arcade.draw_text(output, 20, 20, arcade.color.BLACK)

        # to check if all coins have been collected
        if len(self.coin_sprite_list) ==0:
            arcade.draw_text("GAME OVER", 250, 300, arcade.color.RED, 40)

    def update(self, deltatime):

        # prints 'game over' when all the coins have been collected
        if len(self.coin_sprite_list) ==0:
            arcade.draw_text("GAME OVER", 350, 300, arcade.color.BLACK)

        # the if statement freezes the game when the all the coins are collected
        if len(self.coin_sprite_list) > 0:
            self.coin_sprite_list.update()
            self.tank_sprite_list.update()
            self.rock_sprite_list.update()

            # collision test
            coin_hit_list = arcade.check_for_collision_with_list(self.tank_sprite, self.coin_sprite_list)
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score+=1
                arcade.play_sound(self.coin_sound)
            rock_hit_list= arcade.check_for_collision_with_list(self.tank_sprite, self.rock_sprite_list)
            self.hit_score = 0
            for rock in rock_hit_list:
                rock.remove_from_sprite_lists()
                self.score-=1
                self.sound=arcade.play_sound(self.rock_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.tank_sprite.change_y +=TANK_SPEED
        if key == arcade.key.DOWN:
            self.tank_sprite.change_y -=TANK_SPEED
        if key == arcade.key.RIGHT:
            self.tank_sprite.change_x += TANK_SPEED
        if key == arcade.key.LEFT:
            self.tank_sprite.change_x -=TANK_SPEED
        if key == arcade.key.SPACE:
            self.tank_sprite.change_x=0
            self.tank_sprite.change_y=0

    def on_mouse_motion(self, x, y, dx, dy):

        # the if statement freezes the screen when all the coins are collected
        if len(self.coin_sprite_list)>0:
            self.tank_sprite.center_x = x
            self.tank_sprite.center_y = y
            self._mouse_visible=True


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()