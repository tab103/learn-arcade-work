""" Sprite Sample Program """
import math
import random
import arcade



# --- Constants ---
SPRITE_SCALING_PLAYER = 0.07
SPRITE_SCALING_RING = 0.2
SPRITE_SCALING_BOMB = 0.1
RING_COUNT = 30
BOMB_COUNT = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ring_sound = arcade.load_sound("ring_sound.mp3")
bomb_sound = arcade.load_sound("bomb_sound.wav")


class Ring(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

class Bomb(arcade.Sprite):

    def update(self):
        self.center_x -= 1
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


        # Variables that will hold sprite lists
        self.player_list = None
        self.ring_list = None
        self.bomb_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

# idk setting up a class fot the rings?




    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ring_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()

        # Score
        self.score = 0
        # Tails sprite
        self.player_sprite = arcade.Sprite("tails_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Placing the rings
        for i in range(RING_COUNT):

            ring = Ring("ring_sprite.png", SPRITE_SCALING_RING)

            ring.center_x = random.randrange(SCREEN_WIDTH)
            ring.center_y = random.randrange(SCREEN_HEIGHT)
            self.ring_list.append(ring)

        # Placing the bombs
        for i in range(BOMB_COUNT):

            bomb = Bomb("bomb_sprite.png", SPRITE_SCALING_BOMB)
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            self.bomb_list.append(bomb)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ring_list.draw()
        self.player_list.draw()
        self.bomb_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.ring_list.update()
        self.bomb_list.update()

        # Generate a list of all sprites that collided with the player.
        ring_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.ring_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for ring in ring_hit_list:
            ring.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(ring_sound)

        bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.bomb_list)

        for bomb in bomb_hit_list:
            bomb.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(bomb_sound)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()