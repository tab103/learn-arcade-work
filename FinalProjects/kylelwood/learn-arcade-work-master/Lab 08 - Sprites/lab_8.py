"""You are a pilot tasked with collecting bombs before they fall on the city.
    Collect the bombs while avoiding other aircraft"""

import random
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Falling Bombs"
CHARACTER_SCALING = .15
MOVEMENT_SPEED = 2.5
BOMB_COUNT = 35
ENEMY_COUNT = 12
ENEMY_SPRITE_SCALE = .075
SPRITE_SCALE_BOMBS = .0375


def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename, flipped_horizontally=True)]


class Player(arcade.Sprite):
    def __init__(self):
        # Set up parent class
        super().__init__()

    def update(self):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 10:
            self.right = SCREEN_WIDTH - 10

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 10:
            self.top = SCREEN_HEIGHT - 10


class Bomb(arcade.Sprite):

    def update(self):
        self.center_y -= .5

        # Reset bombs that fall off-screen
        if self.top < 0:
            # Reset to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x += -1.675

        # Reset planes that exit the screen
        if self.left < 0:
            self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 60)
            self.center_y = random.randrange(100, SCREEN_HEIGHT)


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE)

        # sprite lists
        self.player_list = None
        self.bomb_list = None
        self.enemy_list = None

        # player info
        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        # Sounds
        self.engine_noise = arcade.load_sound("prop-plane-14513.mp3")
        arcade.play_sound(self.engine_noise)

        self.explosion = arcade.load_sound("big-impact-7054.mp3")

        self.bomb_collected = arcade.load_sound("reload-123781.mp3")

        # Track the current state of what key is pressed

        self.left_pressed = False

        self.right_pressed = False

        self.up_pressed = False

        self.down_pressed = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from pixabay
        self.player_sprite = arcade.Sprite("green-304704_640.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        # Create the enemy planes
        # image from pixabay
        for j in range(ENEMY_COUNT):

            # Instance
            enemy = Enemy("biplane-158327_1280.png", ENEMY_SPRITE_SCALE)

            # Position the enemy
            enemy.center_y = random.randrange(SCREEN_HEIGHT)
            enemy.center_x = random.randrange(SCREEN_WIDTH)

            # Add enemies to the list
            self.enemy_list.append(enemy)

        # Create the bombs
        for i in range(BOMB_COUNT):

            # Create the bomb instance variable
            # Bomb image from pixabay
            bomb = Bomb("bomb-149693_1280.png", SPRITE_SCALE_BOMBS)

            # Position the bombs
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the bombs to the list
            self.bomb_list.append(bomb)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BURNT_ORANGE)
        self.draw_sun()
        self.draw_sea()
        self.draw_sailboat(150, 21)

        # Draw sprite lists
        self.bomb_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

        # Put the text on the screen.
        output = "Bombs Collected: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def draw_sun(self):
        # draw the sun
        arcade.draw_circle_filled(400, 165, 150, arcade.color.SUNRAY)

    def draw_sea(self):
        # draw the sea
        arcade.draw_lrtb_rectangle_filled(0, 800, 70, 0, arcade.color.HONOLULU_BLUE)

    def draw_sailboat(self, x, y):
        # draw a sailboat
        arcade.draw_lrtb_rectangle_filled(380 + x, 420 + x, 60 + y, 50 + y, arcade.color.BLACK)
        arcade.draw_triangle_filled(390 + x, 65 + y, 410 + x, 65 + y, 400 + x, 80 + y, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(399 + x, 401 + x, 70 + y, 50 + y, arcade.color.BLACK)

    def update_player_speed(self):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED

        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):

        """Called whenever a key is pressed."""

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()

        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()

        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()

        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()

        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()

        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()

        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.bomb_list.update()
        self.enemy_list.update()

        # list of all sprites that collide with the player.
        bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for bomb in bomb_hit_list:
            bomb.remove_from_sprite_lists()
            arcade.play_sound(self.bomb_collected)
            self.score += 1

        # Reset enemy planes after collision
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in enemy_hit_list:
            enemy.remove_from_sprite_lists()
            arcade.play_sound(self.explosion)
            self.score -= 3


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
