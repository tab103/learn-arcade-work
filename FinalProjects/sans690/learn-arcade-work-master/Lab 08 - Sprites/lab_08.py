""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_COIN = 0.4
SPRITE_WATER_BOTTLE = 0.04
COIN_COUNT = 50
WATER_BOTTLE_COUNT = 20
MOVEMENT_SPEED = 8
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

coin_sound = arcade.load_sound("arcade_resources_sounds_coin2.wav", False)
water_bottle_sound = arcade.load_sound("arcade_resources_sounds_error4.wav")


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.freeze = False

    # update method in the class Coin
    def update(self):
        if not self.freeze:
            self.center_x += self.change_x
            self.center_y += self.change_y


class Bottle(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.freeze = False

    def update(self):
        if not self.freeze:
            self.center_x += self.change_x
            self.center_y += self.change_y
            # if out of bounds then bounce
            if self.left < 0:
                self.change_x *= -1
            if self.right > SCREEN_WIDTH:
                self.change_x *= -1
            if self.bottom < 0:
                self.change_y *= -1
            if self.top > SCREEN_HEIGHT:
                self.change_y *= -1


class Player(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.freeze = False

    def update(self):
        if not self.freeze:
            self.center_x += self.change_x
            self.center_y += self.change_y


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # variable that holds player list
        self.player_sprite_list = None
        # variable that holds good list
        self.good_item_list = None
        # variable that holds bad list
        self.bad_item_list = None
        # variable that holds player info
        self.player_sprite = None
        # variable that holds score
        self.score = 0
        # the sound player for the coin sound
        self.coin_sound_player = None
        # the sound player for the coin sound
        self.water_bottle_sound_player = None

        # creates instances of the SpriteList from arcade
        self.player_sprite_list = arcade.SpriteList()
        self.good_item_list = arcade.SpriteList()
        self.bad_item_list = arcade.SpriteList()

        # makes mouse invisible in window
        self.set_mouse_visible(False)

    # method of the class that will assign the values to the instance
    def setup(self):
        # assigns an image with the functionality of the Sprite class from arcade, creates an instance of Sprite
        self.player_sprite = Player("output2.png", SPRITE_SCALING_PLAYER)

        # assigns the position to the player_sprite
        self.player_sprite.center_x = 45
        self.player_sprite.center_y = 300
        # adds the player_sprite to the player_list
        self.player_sprite_list.append(self.player_sprite)

        # creates an instance and assigns values, it is also to the good_item_list
        # good item is a coin
        for i in range(COIN_COUNT):
            # assigns image to the instance
            good_sprite = Coin("coinGold_ul.png", SPRITE_SCALING_COIN)
            # assigns the position of the sprite
            good_sprite.center_x = random.randrange(10, SCREEN_WIDTH)
            good_sprite.center_y = random.randrange(10, SCREEN_HEIGHT)
            good_sprite.change_x -= 0
            good_sprite.change_y += 2
            # add the good_sprite to the good_sprite_list
            self.good_item_list.append(good_sprite)

        # bad item is a water bottle
        for i in range(WATER_BOTTLE_COUNT):
            # assigns image to the instance
            bad_sprite = Bottle("water.png", SPRITE_WATER_BOTTLE)
            # assigns position of sprite
            bad_sprite.center_x = random.randrange(SCREEN_WIDTH)
            bad_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_sprite.change_x = random.randrange(-3, 4)
            bad_sprite.change_y = random.randrange(-3, 4)
            self.bad_item_list.append(bad_sprite)

    # method that updates the sprite list
    def update(self, delta_time: float):
        self.player_sprite_list.update()
        self.good_item_list.update()
        # creates a list of good_sprites that collide with player_sprite
        good_item_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_item_list)
        # for the good_sprites that collide, remove it, and add one to the score
        for good_sprite in good_item_hit_list:
            good_sprite.remove_from_sprite_lists()
            self.score += 1
            # as the score gets higher by collecting good item, play the coin sound by coin_sound_player
            self.coin_sound_player = arcade.play_sound(coin_sound)
        # updates bad_item_list
        self.bad_item_list.update()
        # creates a list based on the bad_sprites that collide with player_sprite
        bad_item_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_item_list)
        # for the bad_sprites that collide with player_sprite, remove it, and subtract from the score
        for bad_sprite in bad_item_hit_list:
            bad_sprite.remove_from_sprite_lists()
            self.score -= 1
            # as the score is lowered by collecting bad item, play the error sound by
            self.water_bottle_sound_player = arcade.play_sound(water_bottle_sound, 10)
        # stops user from moving outside window limit to the left
        if self.player_sprite.center_x < 27:
            self.player_sprite.center_x = 45
        # stops user from moving outside window limit to the right
        elif self.player_sprite.center_x > 783:
            self.player_sprite.center_x = 750
        # stops user from moving outside window limit downward
        if self.player_sprite.center_y < 27:
            self.player_sprite.center_y = 48
        # stops user from moving outside window limit upward
        if self.player_sprite.center_y > 583:
            self.player_sprite.center_y = 565
        # for items in good_item_list
        # if the item's center x and y are greater than the screen height, clear the list
        for g in self.good_item_list:
            if g.center_x and g.center_y > SCREEN_HEIGHT + 650:
                self.good_item_list.clear()

        # if the length of good_item_list is equal to 0
        if len(self.good_item_list) == 0:
            # for items in the good_item_list, freeze is true if the list is equal to 0
            for b in self.bad_item_list:
                b.freeze = True
                # clear the list if condition is met
                self.bad_item_list.clear()
            # for players in the player_sprite_list, freeze is true if the list is equal to 0
            for p in self.player_sprite_list:
                # clear the list if condition is met
                p.freeze = True
                self.player_sprite_list.clear()

    # method that defines when key is being pressed
    def on_key_press(self, key: int, modifiers: int):
        # if the user presses the left arrow key
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        # if not pressing left, then right
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        # if not pressing left or right, then down
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        # if not left, right, down, then up
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED

    # method that defines when user is not pressing key
    def on_key_release(self, key: int, modifiers: int):
        # if not pressing left or right
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        # if not pressing down or up
        elif key == arcade.key.DOWN or key == arcade.key.UP:
            self.player_sprite.change_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        # for players in play_sprite_list, draw
        for players in self.player_sprite_list:
            players.draw()
        self.player_sprite_list.draw()
        # for items in good_item_list, draw
        for items in self.good_item_list:
            items.draw()
        # for items in bad_item_list, draw
        for items in self.bad_item_list:
            items.draw()
        # creates the score boards
        output = f" Score : {self.score}"
        arcade.draw_text(output, 10, 580, arcade.color.BLACK, 12, 10)
        # if the length of good_item_list equals 0, create the text and set background
        if len(self.good_item_list) == 0:
            arcade.draw_text("Game Over", 250, 300, arcade.color.WHITE_SMOKE, 40, 5)
            arcade.set_background_color(arcade.color.BLACK)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
