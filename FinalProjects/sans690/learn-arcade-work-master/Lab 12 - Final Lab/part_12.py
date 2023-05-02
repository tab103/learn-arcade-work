from pyglet.math import Vec2
import update_function
import setup_function
import battle
import arcade

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 2
MAP_SCALING = 1.5
CAMERA_SPEED = 0.47
PLAYER_SCALING = 1
# how many pixels to keep between the character and screen edge
VIEWPORT_MARGIN = 250


# Player class inherits arcade's Sprite class
class Player(arcade.Sprite):
    """Initializer"""

    def __init__(self):
        super(Player, self).__init__()
        self.player_sprite = None
        self.player_sprite_list = None
        self.scale = 0
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    def setup_player(self):
        # variable creates instance of arcade class SpriteList
        self.player_sprite_list = arcade.SpriteList()
        scale = PLAYER_SCALING - .3
        # creating an instance of the arcade's animated walking sprite class variable hold file name
        self.player_sprite = arcade.AnimatedWalkingSprite(scale=scale)
        # Credit for images: PurpleZaffre on Deviant Art,
        # https://www.deviantart.com/purplezaffre/art/Unova-Protagonist-Hilbert-696354095
        # Also credit to Nintendo and GameFreak for original concept
        file_name = "Player Resources/pngs/(New)UserGen4.png"
        # creates list of a list
        #  [200, 230, 100, 90], [100, 230, 100, 90]
        image_location_list = [[0, 230, 90, 90]]
        self.player_sprite.stand_right_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        self.player_sprite.stand_left_textures = \
            arcade.load_textures(file_name, image_location_list, True, hit_box_algorithm="Detailed")
        # creates list of a list
        # [[0, 230, 90, 90]
        image_location_list = [[200, 230, 100, 90], [100, 230, 100, 90], [100, 230, 100, 90]]
        self.player_sprite.walk_right_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        self.player_sprite.walk_left_textures = \
            arcade.load_textures(file_name, image_location_list, True, hit_box_algorithm="Detailed")
        image_location_list = [[0, 320, 100, 100], [100, 320, 100, 100], [100, 320, 100, 100], [320, 320, 100, 100]]
        self.player_sprite.walk_up_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        image_location_list = [[0, 0, 90, 100], [100, 0, 130, 100], [100, 0, 130, 100], [320, 0, 100, 100]]
        self.player_sprite.walk_down_textures = \
            arcade.load_textures(file_name, image_location_list, True, hit_box_algorithm="Detailed")
        self.player_sprite_list.append(self.player_sprite)


class NPC(arcade.Sprite):
    """Initializer"""

    def __init__(self):
        super(NPC, self).__init__()
        self.npc_sprite_list = None
        self.npc_sprite = None
        self.scale = 0
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of NPC class that tells the class how to move when called
    def update(self):
        # current x position = current x position plus the change to x
        self.center_x += self.change_x
        # current y position = current y position plus the change to y
        self.center_y += self.change_y
        battle()

    def setup_npc(self):
        # variable creates instance of arcade class SpriteList
        self.npc_sprite_list = arcade.SpriteList()
        scale = PLAYER_SCALING - .76
        # creating an instance of the arcade's animated walking sprite class
        self.npc_sprite = arcade.AnimatedWalkingSprite(scale=scale)
        # variable hold file name
        # Credit for image: Othienka on Deviant Art,
        # https://www.deviantart.com/othienka/art/Team-Rocket-Player-Character-595571094
        # Also credit to Nintendo and GameFreak for original concept
        file_name = "Player Resources/pngs/TeamRocketGruntGen4.png"
        # creates list of a list
        # [300, 655, 300, 300], [0, 655, 300, 300], [960, 655, 300, 300]
        image_location_list = [[0, 655, 300, 300]]
        self.npc_sprite.stand_right_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        self.npc_sprite.stand_left_textures = \
            arcade.load_textures(file_name, image_location_list, True, hit_box_algorithm="Detailed")
        # creates list of a list
        # [0, 655, 300, 300]
        image_location_list = [[300, 655, 300, 300], [600, 655, 300, 300], [960, 655, 300, 300]]
        self.npc_sprite.walk_right_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        self.npc_sprite.walk_left_textures = \
            arcade.load_textures(file_name, image_location_list, True, hit_box_algorithm="Detailed")
        image_location_list = [[0, 902, 300, 430], [300, 902, 300, 430], [600, 902, 300, 430], [960, 902, 300, 430]]
        self.npc_sprite.walk_up_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        image_location_list = [[0, 0, 300, 300], [300, 0, 300, 300], [600, 0, 300, 300], [960, 0, 300, 300]]
        self.npc_sprite.walk_down_textures = \
            arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")
        self.npc_sprite_list.append(self.npc_sprite)


class Monster(arcade.Sprite):
    """Initializer"""

    def __init__(self):
        super(Monster, self).__init__()
        self.scale = 0
        self.health = 0
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of Monster class that tells the class how to move when called
    def update(self):
        # current x position = current x position plus the change to x
        self.center_x += self.change_x
        # current y position = current y position plus the change to y
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """Initializer"""

    def __init__(self, ):
        # calls that parent class arcade.Window and inherits the methods/attributes/functions of that class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Something")
        # sets attributes to the class
        # empty variables is set
        self.tile_map = None
        self.animate_frame_count = 0
        self.monster_sprite = None
        # creates camera for player
        self.camera_sprite = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics_engine = None
        self.current_room = 0
        # lists
        self.monster_sprite_list = arcade.SpriteList()
        self.room_list = []

    def load_level(self):
        load_level_function.load_level(self)

    # sets up the game, defines the values for objects and anything else in the game
    def setup(self):
        Player.setup_player(self)
        NPC.setup_npc(self)
        setup_function.setup_game(self)

    def update(self, delta_time: float):
        update_function.update(self)

    # when the key is pressed the player is moved
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

    # when the player releases the key
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

    def scroll_to_player(self):
        # based on where the player is, the camera will position to be centered on player
        # so window width is 800, player is at 100, 800/2 = 400, 100 - 400 = -300, so camera will start at -300
        position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
        # camera will move to position at set speed
        self.camera_sprite.move_to(position, CAMERA_SPEED)

    def on_resize(self, width: float, height: float):
        # resizes the window when player hits edge
        self.camera_sprite.resize(int(width), int(height))

    def on_draw(self):
        arcade.start_render()
        # selects the camera to use for player sprite
        self.camera_sprite.use()
        arcade.set_background_color(arcade.color.BLACK)

        # Bedroom
        if self.current_room == 0:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Carpets"].draw()
            self.tile_map.sprite_lists["Tables"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
            self.tile_map.sprite_lists["Filter"].draw()
            self.tile_map.sprite_lists["Bed"].draw()
            self.tile_map.sprite_lists["Sheet"].draw()

        # Downstairs
        elif self.current_room == 1:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Carpets"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
            self.tile_map.sprite_lists["Tables"].draw()
            self.tile_map.sprite_lists["Filter"].draw()

        # Outside
        elif self.current_room == 2:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Shadows"].draw()
            self.tile_map.sprite_lists["Trees"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
            self.tile_map.sprite_lists["Trees(with collision)"].draw()
            self.tile_map.sprite_lists["Buildings"].draw()
            self.tile_map.sprite_lists["Fence"].draw()
            self.tile_map.sprite_lists["Filter"].draw()

        # Wild
        elif self.current_room == 3:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Grass"].draw()
            self.tile_map.sprite_lists["Trees(with collision)"].draw()
            self.tile_map.sprite_lists["Trees"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
            self.tile_map.sprite_lists["Filter"].draw()
            self.tile_map.sprite_lists["Fence"].draw()
            self.tile_map.sprite_lists["Npc"].draw()
            self.npc_sprite_list.draw()

        # Forest
        elif self.current_room == 4:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Fence"].draw()
            self.tile_map.sprite_lists["Grass"].draw()
            self.tile_map.sprite_lists["Trees(with collision)"].draw()
            self.tile_map.sprite_lists["Trees"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
            self.tile_map.sprite_lists["Filter"].draw()

        self.player_sprite_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
    
