import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BANANA = 0.2
BANANA_COUNT = 50
BBANANA_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Banana(arcade.Sprite):

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Bbanana(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0
        self.bounce = arcade.load_sound("bounce.wav")
        self.bounce_player = None

    def on_update(self, delta_time: float = 1 / 6) -> 0:

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Lab")

        self.player_list = None
        self.banana_list = None
        self.bbanana_list = None
        self.bounce = arcade.load_sound("bounce.wav")
        self.bounce_player = None
        self.banana = arcade.load_sound("banana.wav")
        self.banana_player = None
        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.FOREST_GREEN)

    def setup(self):

        # Sprite list
        self.player_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.bbanana_list = arcade.SpriteList()

        self.score = 0

        # Character
        # https://www.shareicon.net/ape-monkey-zoo-animals-mammal-wild-life-animal-kingdom-813908
        self.player_sprite = arcade.Sprite("Monkey.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # makes bananas
        # https://www.flaticon.com/free-icon/banana_286681
        # https://clipart-library.com/clipart/1713450.htm
        for i in range(BANANA_COUNT):
            banana = Banana("Banana.png", SPRITE_SCALING_BANANA)

            # position
            banana.center_x = random.randrange(SCREEN_WIDTH)
            banana.center_y = random.randrange(SCREEN_HEIGHT)

            self.banana_list.append(banana)

        for i in range(BBANANA_COUNT):
            bbanana = Bbanana("BadBanana.png", SPRITE_SCALING_BANANA)

            # position
            bbanana.center_x = random.randrange(SCREEN_WIDTH)
            bbanana.center_y = random.randrange(SCREEN_HEIGHT)
            bbanana.change_x = random.randrange(-3, 4)
            bbanana.change_y = random.randrange(-3, 4)

            self.bbanana_list.append(bbanana)

    def on_draw(self):
        arcade.start_render()
        self.banana_list.draw()
        self.bbanana_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.banana_list) == 0:
            arcade.draw_text("GAME OVER", 300, 300, arcade.color.WHITE, 20)

        # Mouse Motion
    def on_mouse_motion(self, x, y, dx, dy):
        if not len(self.banana_list) == 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        if not len(self.banana_list) == 0:
            self.banana_list.update()
            bananas_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.banana_list)
            for banana in bananas_hit_list:
                banana.remove_from_sprite_lists()
                self.score += 1
                if not self.banana_player or not self.banana_player.playing:
                    self.banana_player = arcade.play_sound(self.banana)
            self.bbanana_list.on_update()
            bbananas_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bbanana_list)
            for bbanana in bbananas_hit_list:
                bbanana.remove_from_sprite_lists()
                self.score -= 1
                if not self.bounce_player or not self.bounce_player.playing:
                    self.bounce_player = arcade.play_sound(self.bounce)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
