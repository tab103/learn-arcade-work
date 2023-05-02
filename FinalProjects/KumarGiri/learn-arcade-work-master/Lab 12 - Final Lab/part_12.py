"""
All the codes, I used for this lab, I got from the arcade website or from previous lab assignments
I have cited the external audios and sprite images I have used.
"""


import arcade
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 550
SCREEN_TITLE = "Final Project"

GRAVITY = 1
PLAYER_MOVEMENT_SPEED = 5
PLAYER_JUMP_SPEED = 16
STAR_SPEED = 9

PLAYER_SCALING = 0.25
GRASS_SCALING = 0.5
COIN_SCALING = 0.2


# instructions for the spinning star to avoid
class Star(arcade.Sprite):
    def __init__(self, file_name, sprite_scaling):
        super().__init__(file_name, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = STAR_SPEED
        self.speed = 0
        self.change_angle = 10

    # movement and bouncing
    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.change_x = -STAR_SPEED
        elif self.center_x == 0:
            self.change_x = STAR_SPEED

        # Rotate the star
        self.angle += self.change_angle


# Player avatar
class Player(arcade.Sprite):
    def __init__(self, file_name, sprite_scaling):
        super().__init__(file_name, sprite_scaling)
        self.center_x = 0
        self.center_y = 0

    # left and right boundaries
    def update(self):
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        elif self.center_x < 0:
            self.center_x = SCREEN_WIDTH


#  grass platforms and the coins on top
class GrassPlatform(arcade.Sprite):
    def __init__(self, file_name, sprite_scaling):
        super().__init__(file_name, sprite_scaling)
        self.center_x = 0
        self.center_y = 0

        # coin image from Kenney.nl, URL: https://www.kenney.nl/assets/puzzle-pack-2
        self.coin = arcade.Sprite("images/coin.png", COIN_SCALING)
        self.coin.center_x = 0
        self.coin.center_y = 0

    # moving platform downward and materializing from the top
    def update(self):
        self.center_y -= GRAVITY
        if self.center_y == 30:
            self.center_y = SCREEN_HEIGHT
            self.center_x += 35
        if self.center_x >= SCREEN_WIDTH:
            self.center_x = 0

        # # coin movement logic
        self.coin.center_y -= GRAVITY
        if self.coin.center_y == 30:
            self.coin.center_y = SCREEN_HEIGHT
            self.coin.center_x += 35


# function to build the star
def star(self):
    # star_bronze from Kenney.nl, URL: https://www.kenney.nl/assets/space-shooter-redux
    self.star_sprite = Star("images/star_bronze.png", sprite_scaling=0.8)
    self.star_sprite.center_x = 0
    self.star_sprite.center_y = 55
    self.star_list.append(self.star_sprite)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Load Sounds

        # coin_collection sound from mixkit.co, URL:https://mixkit.co/free-sound-effects/coin/
        self.coin_sound = arcade.load_sound("sounds/coin collection.wav")

        # jump sound from mixkit.co , URL: https://mixkit.co/free-sound-effects/jump/
        self.jump_sound = arcade.load_sound("sounds/jump.wav")

        # hurt sound from mixkit.co, URL: https://mixkit.co/free-sound-effects/hurt/
        self.hurt_sound = arcade.load_sound("sounds/hurt.wav")

        # game_over sound from mixkit.com, URL: https://mixkit.co/free-sound-effects/game/
        self.game_over_sound = arcade.load_sound("sounds/game over.wav")
        self.game_over_sound_player = None

        self.one_grass = None
        self.background = None

        # default values to start
        self.score = 0
        self.lives = 5

        self.player_sprite = None
        self.star_sprite = None

        self.player_list = None
        self.pavement_list = None
        self.grass_list = None
        self.coin_list = None
        self.star_list = None

        # switch to play the game_over sound only once
        self.done = False

        # adds physical properties
        self.physics_engine = None

        # background color, behind the texture
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        # Adds the background scenery

        # colored_forest image from Kenney.nl URL: https://www.kenney.nl/assets/background-elements
        self.background = arcade.load_texture("images/colored_forest.png")

        self.player_list = arcade.SpriteList()
        self.pavement_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Load Player Sprite
        # character_robot_idle.png image from Kenney.nl, URL: https://www.kenney.nl/assets/toon-characters-1
        self.player_sprite = Player("images/character_robot_idle.png", PLAYER_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # Pavement at the bottom
        # wall.png image from Kenney.nl, URL: https://www.kenney.nl/assets/platformer-art-pixel-redux
        for x in range(0, SCREEN_WIDTH, 30):
            pavement = arcade.Sprite("images/wall.png")
            pavement.center_x = x
            pavement.center_y = 5
            self.pavement_list.append(pavement)

        # setting up the bronze star that moves along the pavement
        star(self)

        # initial coordinates to draw the platforms
        list_of_coordinates = [[30, 125], [285, 175], [430, 125]]

        # randomizes the coordinates in the list above
        count = 0
        while count < 4:
            for times in range(3):
                for coordinates in list_of_coordinates:
                    for x in range(coordinates[0], coordinates[0] + 100, 35):
                        # grass.png image from Kenney.nl, URL: https://www.kenney.nl/assets/block-pack
                        grass = GrassPlatform("images/grass.png", GRASS_SCALING)
                        grass.center_x = x
                        grass.center_y = coordinates[1]
                        self.grass_list.append(grass)
                        if random.randrange(3) == 1:
                            grass.coin.center_x = x
                            grass.coin.center_y = coordinates[1] + 20
                            self.coin_list.append(grass.coin)

                list_of_coordinates[times][1] += 95
                list_of_coordinates[times][0] += 40
            count += 1

        # applies gravity to the Player, and makes pavement and platform solid.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant=GRAVITY,
                                                             walls=self.pavement_list, platforms=self.grass_list)

    def on_draw(self):
        self.clear()

        # only draws when the player has lives
        if self.lives > 0:
            # Background texture
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

            self.player_list.draw()
            self.grass_list.draw()
            self.coin_list.draw()
            self.pavement_list.draw()
            self.star_list.draw()

            # Draws the score and lives
            output = f"score: {self.score}\tlives: {self.lives}"
            arcade.draw_text(output, 20, 20, arcade.color.BLACK)

        # when lives are used up, draws the 'game over' screen
        if self.lives == 0:
            arcade.draw_text("GAME OVER", 150, 300, color=arcade.color.RED, font_size=28)
            arcade.draw_text(f'Score: {self.score}', 150, 250, color=arcade.color.BLUE, font_size=16)
            arcade.draw_text('To Continue with +1 life, press SPACE', 150, 200, color=arcade.color.BLUE, font_size=16)

    def on_key_press(self, key, modifiers):

        # movement of the Player using keys
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

            # plays jumping sound effects
            arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Regain lives when 'space' pressed
        if key == arcade.key.SPACE:
            self.lives = 1
            self.score = 0
            self.done = False

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        # playable elements only updated when player has lives
        if self.lives > 0:
            self.player_list.update()
            self.grass_list.update()
            self.coin_list.update()
            self.star_list.update()
            self.physics_engine.update()

            # checking coin collisions with player sprite, adding score, and playing coin sound effect
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.coin_sound)

            # checking collision with player sprite and spinning star, play hurt sound effect
            lives_check_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
            for hit in lives_check_list:
                hit.remove_from_sprite_lists()
                self.lives -= 1

                # after removing the star, draw the star at its original place
                star(self)
                arcade.play_sound(self.hurt_sound)

        # check game over condition and play sound
        if self.lives == 0:
            if not self.done:
                if not self.game_over_sound_player or not self.game_over_sound_player.playing:
                    self.game_over_sound_player = arcade.play_sound(self.game_over_sound)
                    self.done = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
