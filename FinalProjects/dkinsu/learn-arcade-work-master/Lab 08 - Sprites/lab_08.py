""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 3.0
SPRITE_SCALING_RING = 1.5
SPRITE_SCALING_FIRE = 1.5
RING_COUNT = 50
FIRE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initializing class for
class Ring(arcade.Sprite):
    def update(self):
        # Downward movement
        self.center_y -= 1
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class Fire(arcade.Sprite):
    def update(self):
        # Left movement
        self.center_x -= 1
        if self.right < 0:
            self.left = SCREEN_WIDTH

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.ring_list = None
        self.fire_list = None

        # Game over variable
        self.game_over = False

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.vine_boom = arcade.load_sound("vine-boom.wav")
        self.ring_sound = arcade.load_sound("arcade_resources_sounds_hurt2.wav")

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ring_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl micro-roguelike
        self.player_sprite = arcade.Sprite("tile_0004.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the rings
        for i in range(RING_COUNT):

            # Create the ring instance
            # ring image from kenney.nl micro-roguelike
            ring = Ring("tile_0089.png", SPRITE_SCALING_RING)

            # Position the ring
            ring.center_x = random.randrange(SCREEN_WIDTH)
            ring.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the ring to the lists
            self.ring_list.append(ring)

        for i in range(FIRE_COUNT):

            # Creating fire instance
            # fire image from kenney.nl micro-roguelike
            fire = Fire("tile_0136.png", SPRITE_SCALING_FIRE)

            # Positioning fire
            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            self.fire_list.append(fire)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ring_list.draw()
        self.fire_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if self.game_over == True:
            arcade.draw_text("Game Over", 240, 300, arcade.color.WHITE, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if not self.game_over:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if not self.game_over:
            # Call update on all sprites - movement
            self.ring_list.update()
            self.fire_list.update()

        # Generate a list of all sprites that collided with the player.
        rings_hit_lists_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.ring_list)
        fire_hit_lists_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.fire_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        # Playing sound on collision as well
        for ring in rings_hit_lists_hit_list:
            ring.remove_from_sprite_lists()
            arcade.play_sound(self.ring_sound, 0.6)
            self.score += 1

        # Reducing score for bad sprites
        # Playing sound on collision as well
        for fire in fire_hit_lists_hit_list:
            fire.remove_from_sprite_lists()
            arcade.play_sound(self.vine_boom, 0.2)
            self.score -= 1
        if len(self.ring_list) == 0:
            self.game_over = True
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()