""" Sprite Sample Program """
# Credits: Sound Effect from
# <a href="https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=43831">Pixabay</a>
import random
import arcade



# --- Constants ---
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_ENEMY = 1
SPRITE_SCALING_BULLET = 0.02
BULLET_SPEED = 5
SPRITE_SCALING_ASTEROID = 0.3
ASTEROID_COUNT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Chao in Space"



class Asteroid(arcade.Sprite):

    def update(self):
        self.center_x -= 1
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH

class Enemy(arcade.Sprite):
    # add the location of the enemy

    def update(self):
        self.enemy_sprite = arcade.Sprite("dark_chao_sprite.png", SPRITE_SCALING_ENEMY)
        self.enemy_sprite.center_x = self.player_sprite.center_x
        self.enemy_sprite.center_y = self.player_sprite.center_y
        self.enemy_list.append(self.enemy_sprite)
class Bullet(arcade.Sprite):
    # Call update on all sprites
    def on_mouse_press(self):
        bullet = arcade.Sprite("bullet_sprite.png", SPRITE_SCALING_BULLET)
        # location of the bullets where the player is
        self.player_sprite = arcade.Sprite("chao_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        arcade.play_sound = ("laser_sound.mp3", SPRITE_SCALING_BULLET)
        self.player_list.append(self.player_sprite)

class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()

        def __init__(self):
            """ This is run once when we switch to this view """
            super().__init__()
            self.texture = arcade.load_texture("title.jpg")
            arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("game_over.webp")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)





class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()


        # Variables that will hold sprite lists
        self.player_list = None
        self.asteroid_list = None
        self.bullet_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)
        # background shenanigans
        self.background = arcade.load_texture("space.jfif")


    def on_update(self, delta_time):
        self.bullet_list.update()

        # Loop through each bullet


    def setup(self):
        """ Set up the game and initialize the variables. """
        self.background = arcade.load_texture("space.jfif")
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0
        # Chao sprite
        self.player_sprite = arcade.Sprite("chao_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        # Placing the asteroids
        for i in range(ASTEROID_COUNT):

            asteroid = Asteroid("asteroid_sprite.png", SPRITE_SCALING_ASTEROID)
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_list.append(asteroid)



    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.player_list.draw()
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        # Gunshot sound

        # Create a bullet
        bullet = arcade.Sprite("laser_sprite.png", SPRITE_SCALING_BULLET)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 0

        # Give the bullet a speed
        bullet.change_x = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.center_y = self.player_sprite.center_y

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists(),

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound


            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
# bullet motions


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.asteroid_list.update()
        self.enemy_list.update()

        # Generate a list of all sprites that collided with the player.

        # Loop through each colliding sprite, remove it, and add to the score.

        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)

        for asteroid in asteroid_hit_list:
            asteroid.remove_from_sprite_lists()
            self.score -= 1



def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()