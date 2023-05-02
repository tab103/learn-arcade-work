import random
import arcade
# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_METEORITE = .10
COIN_COUNT = 50
SPRITE_SCALING_MONEY = .05

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"


class Coin(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_y -= 1
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT


class Bad_sprite(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_x -= 1
        if self.center_x == 0:
            self.center_x = SCREEN_WIDTH


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bad_sprite = None
        self.game_over = None
        self.freeze = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # sound
        self.belt_sound = arcade.load_sound("beltHandle1.ogg")
        self.knifeslice = arcade.load_sound("knifeSlice.ogg")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_sprite = arcade.SpriteList()
        self.game_over = arcade.SpriteList()
        self.freeze = arcade.SpriteList()


        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("money_sign.png", SPRITE_SCALING_MONEY)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # create bad sprite
        for i in range(15):
            # Create the coin instance
            # Coin image from kenney.nl
            sprite = Bad_sprite("meteorite.png", SPRITE_SCALING_METEORITE)

            # Position the coin
            sprite.center_x = random.randrange(SCREEN_WIDTH)
            sprite.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.bad_sprite.append(sprite)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()
        self.bad_sprite.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)
        if len(self.coin_list) == 0:
            arcade.draw_text("Game over", 200, 300, arcade.color.BLUE, 75)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        if not self.freeze:
            self.coin_list.update()
            self.bad_sprite.update()
            if len(self.coin_list) == 0:
                self.freeze = True

            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                  self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.belt_sound)

            bad_sprite_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite)
            for bad_sprite in bad_sprite_hit_list:
                bad_sprite.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.knifeslice)



def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
