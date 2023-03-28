# Dynamic Attributes
# https://www.codingninjas.com/codestudio/library/dynamic-attributes-and-properties-python#:~:text=Dynamic%20Attributes%20are%20the%20attributes,attributes'%20dynamicity%20and%20their%20security.

import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_LASER = 0.8
METEOR_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 10

class Bullet(arcade.Sprite):
    def __init__(self, file, scale, shooter):
        super().__init__(file, scale)
        self.shooter = shooter

        # The image points to the right, and we want it to point up. So
        # rotate it.
        self.angle = 0

        # Position the bullet
        self.center_x = self.shooter.center_x
        self.bottom = self.shooter.top

    def update(self):
        # If the bullet flies off-screen, remove it.
        if self.bottom > SCREEN_HEIGHT:
            self.remove_from_sprite_lists()

        self.center_y += BULLET_SPEED
        self.center_x = self.shooter.center_x


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.player_list = None
        self.meteor_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("images/ship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the meteors
        for i in range(METEOR_COUNT):

            # Create the meteor instance
            # Create a random scale between .3 and .8
            scale = float(random.randrange(2,6) / 10)

            meteor = arcade.Sprite("images/meteor.png", scale)

            # Position the meteor
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(120, SCREEN_HEIGHT)
            meteor.change_x -= random.randrange(2, 5)

            # Add the meteor to the lists
            self.meteor_list.append(meteor)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.meteor_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = Bullet("images/laser.png", SPRITE_SCALING_LASER, self.player_sprite)

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.meteor_list.update()
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a meteor
            hit_list = arcade.check_for_collision_with_list(bullet, self.meteor_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every meteor we hit, add to the score and remove the meteor
            for meteor in hit_list:
                meteor.remove_from_sprite_lists()
                self.score += 1

        for meteor in self.meteor_list:

            meteor.angle += 1
            if meteor.center_x < 0:
                meteor.remove_from_sprite_lists()
                scale = float(random.randrange(2, 6) / 10)
                meteor = arcade.Sprite("images/meteor.png", scale)
                meteor.change_x -= random.randrange(1, 5)
                # Position the meteor
                meteor.center_x = random.randrange(SCREEN_WIDTH + 200)
                meteor.center_y = random.randrange(120, SCREEN_HEIGHT)
                # Add the meteor to the lists
                self.meteor_list.append(meteor)

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()