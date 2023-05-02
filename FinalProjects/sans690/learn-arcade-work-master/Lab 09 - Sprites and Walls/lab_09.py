import random
import arcade
from pyglet.math import Vec2

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Speed
MOVEMENT_SPEED = 1
MOVEMENT_CRAB_SPEED = 0.8
# Scaling
SPRITE_FENCE_SCALING = 1
SPRITE_PLAYER_SCALING = 1.5
SPRITE_COIN_SCALING = 0.2
SPRITE_GRASS_SCALING = 0.9
# Amount
COIN_COUNT = 50
TREE_COUNT = 30
# Sound
coin_sound = arcade.load_sound("Lab 9 - Resources/sounds/arcade_resources_sounds_coin2.wav")
bump_sound = arcade.load_sound("Lab 9 - Resources/sounds/jump.wav", False)
# Sound from Nintendo

# sound from Nintendo
theme_sound = arcade.load_sound("Lab 9 - Resources/sounds/Pallet Town Theme.wav", False)
# how many pixels to keep between the character and screen edge
VIEWPORT_MARGIN = 220
# camera moves how fast to the player
CAMERA_SPEED = 0.8


# Grass class inherits functionality of arcade.Sprite
class Grass(arcade.Sprite):
    def __init__(self, filename, SPRITE_GRASS_SCALING):
        super(Grass, self).__init__(filename, SPRITE_GRASS_SCALING)
        # attributes of the Grass class
        self.grass_sprite = None
        # position of the grass image
        self.center_x = 0
        self.center_y = 0


# Fence class inherits functionality of arcade.Sprite
class Fence(arcade.Sprite):
    def __init__(self, filename, SPRITE_FENCE_SCALING):
        super(Fence, self).__init__(filename, SPRITE_FENCE_SCALING)
        # attributes of the Fence class, the fence
        self.left_fence_corner_sprite = None
        self.right_fence_corner = None
        self.opening_for_fence_sprite = None
        self.middle_upward_fence_sprite = None
        self.middle_connector_sprite = None
        self.end_fence_sprite = None
        # attributes of the Fence class, position of the fence image
        self.center_x = 0
        self.center_y = 0


# Wall class inherits functionality of arcade.Sprite
class Wall(arcade.Sprite):
    def __init__(self, filename, SPRITE_FENCE_SCALING):
        super(Wall, self).__init__(filename, SPRITE_FENCE_SCALING)
        # attributes of the Wall class, the wall
        self.left_wall_corner_sprite = None
        self.right_wall_corner = None
        self.opening_for_wall_sprite = None
        self.middle_upward_wall_sprite = None
        self.middle_wall_connector_sprite = None
        # attributes of the Wall class, position of the wall image
        self.center_x = 0
        self.center_y = 0


# House class inherits functionality of arcade.Sprite
class House(arcade.Sprite):
    def __init__(self, filename, SPRITE_PLAYER_SCALING):
        super(House, self).__init__(filename, SPRITE_PLAYER_SCALING)
        # attributes of the House class, the house
        self.roof_sprite = None
        self.wall_sprite = None
        # attributes of the House class, position of the house image
        self.center_x = 0
        self.center_y = 0


# Coin class inherits functionality of arcade.Sprite
class Coin(arcade.Sprite):
    def __init__(self, filename, SPRITE_COIN_SCALING):
        super(Coin, self).__init__(filename, SPRITE_COIN_SCALING)
        # attribute of the Coin class, position on the coins
        self.center_x = 0
        self.center_y = 0
        # change in position
        self.change_x = 0
        self.change_y = 0

    # method that updates the coin sprite
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y


# Player class inherits functionality of arcade.Sprite

class Player(arcade.Sprite):
    def __init__(self, filename, SPRITE_PLAYER_SCALING):
        super(Player, self).__init__(filename, SPRITE_PLAYER_SCALING)
        # attributes of the Player class, player image
        self.player_sprite = None
        # attributes of the Player class, position of the player
        self.center_x = 0
        self.center_y = 0
        # change in position
        self.change_x = 0
        self.change_y = 0

    # method that updates the position of the player
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y


class Crab(arcade.Sprite):
    def __init__(self, filename, SPRITE_PLAYER_SCALING):
        super(Crab, self).__init__(filename, SPRITE_PLAYER_SCALING)
        # attributes of the Crab class, crab image
        self.crab_sprite = None
        # attributes of the Crab class, position of the crab
        self.center_x = 0
        self.center_y = 0
        # change in position
        self.change_x = 0
        self.change_y = 0

    # method that updates the position of the crab
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y

    # method in Crab class
    def follow_sprite(self, player_sprite):
        # if center_y of Crab class is greater than player_sprite.center_y
        if self.center_y < player_sprite.center_y:
            # center_y of Crab class = center_y of Crab class + min crab speed,
            # player_sprite.center_y - center_y of Crab class
            self.center_y += min(MOVEMENT_CRAB_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(MOVEMENT_CRAB_SPEED, self.center_y - player_sprite.center_y)
        if self.center_x < player_sprite.center_x:
            self.center_x += min(MOVEMENT_CRAB_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(MOVEMENT_CRAB_SPEED, self.center_x - player_sprite.center_x)


# MyGame class inherits functionality of arcade.Window
class MyGame(arcade.Window):
    """Initializer"""

    def __init__(self):
        # calls the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "SPRITES AND WALLS")
        # variables that holds physics engine
        self.player_hit_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.physics_engine1 = None
        self.physics_engine2 = None
        self.physics_engine3 = None
        self.physics_engine4 = None
        self.bump_sound_player = None
        # variable that hold score info
        self.score = 0
        # variable hold info for sound player
        self.coin_sound_player = None
        # creates camera, one for score and other for player sprite
        self.camera_sprite = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        # gives the list the functions/methods/attributes of the class
        self.fence_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()
        self.house_list = arcade.SpriteList()
        self.tree_list = arcade.SpriteList()

    def setup(self):
        # sets background
        arcade.set_background_color(arcade.color.WHITE)
        # plays theme_sound
        arcade.play_sound(theme_sound, volume=0.3)
        for coin in range(COIN_COUNT):
            # variable that defines the image of the coin, instance creation
            coin = Coin("Lab 9 - Resources/coinGold_ul copy.png", SPRITE_COIN_SCALING)
            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False
            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(30, SCREEN_WIDTH - 100)
                coin.center_y = random.randrange(30, SCREEN_HEIGHT - 100)
                # See if the coin is hitting a fence/wall
                fence_hit_list = arcade.check_for_collision_with_list(coin, self.fence_list)
                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)
                # See if coin is hitting a tree
                coin_hit_tree_list = arcade.check_for_collision_with_list(coin, self.tree_list)
                if len(fence_hit_list) == 0 and len(coin_hit_list) == 0 and len(coin_hit_tree_list) == 0:
                    # It is!
                    coin_placed_successfully = True
                    # Add the coin to the lists
                    self.coin_list.append(coin)
        """box fence 1"""
        # variables that defines the image of the fence, creates an instances of the class
        left_fence_corner_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0068.png", SPRITE_FENCE_SCALING)
        # position
        left_fence_corner_sprite.center_x = 385
        left_fence_corner_sprite.center_y = 400
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite)
        # instance creation
        left_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0044.png",
                                          SPRITE_FENCE_SCALING)
        # position
        left_fence_corner_sprite1.center_x = 385
        left_fence_corner_sprite1.center_y = 500
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite1)
        # instance creation
        right_fence_corner_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0070.png",
                                          SPRITE_FENCE_SCALING)
        # position
        right_fence_corner_sprite.center_x = 700
        right_fence_corner_sprite.center_y = 400
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite)
        # instance creation
        right_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0046.png",
                                           SPRITE_FENCE_SCALING)
        # position
        right_fence_corner_sprite1.center_x = 700
        right_fence_corner_sprite1.center_y = 500
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite1)
        for fence in range(410, 500, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 385
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(410, 500, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 700
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(400, 700, 15):
            # instance creation
            middle_connector_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                            SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 400
            self.fence_list.append(middle_connector_sprite)
        for fence in range(400, 700, 15):
            # instance creation
            middle_connector_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                            SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 500
            self.fence_list.append(middle_connector_sprite)

        """box fence 2"""
        # variables that defines the image of the fence, creates an instances of the class
        left_fence_corner_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0068.png", SPRITE_FENCE_SCALING)
        # position
        left_fence_corner_sprite.center_x = 385
        left_fence_corner_sprite.center_y = 250
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite)
        # instance creation
        left_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0044.png",
                                          SPRITE_FENCE_SCALING)
        # position
        left_fence_corner_sprite1.center_x = 385
        left_fence_corner_sprite1.center_y = 350
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite1)
        # instance creation
        right_fence_corner_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0070.png",
                                          SPRITE_FENCE_SCALING)
        # position
        right_fence_corner_sprite.center_x = 700
        right_fence_corner_sprite.center_y = 250
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite)
        # instance creation
        right_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0046.png",
                                           SPRITE_FENCE_SCALING)
        # position
        right_fence_corner_sprite1.center_x = 700
        right_fence_corner_sprite1.center_y = 350
        self.fence_list.append(right_fence_corner_sprite1)
        for fence in range(400, 700, 15):
            # instance creation
            middle_connector_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                            SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 350
            self.fence_list.append(middle_connector_sprite)
        for fence in range(400, 700, 15):
            # instance creation
            middle_connector_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                            SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 250
            self.fence_list.append(middle_connector_sprite)
        for fence in range(260, 345, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 385
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(260, 345, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 700
            middle_upward_fence_sprite.center_y = fence
            # fence_list adds sprite to the fence_list
            self.fence_list.append(middle_upward_fence_sprite)

        """outside fence"""
        for wall in range(20, 790, 16):
            # instance creation
            middle_wall_connector_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0097.png",
                                                SPRITE_FENCE_SCALING)
            # position
            middle_wall_connector_sprite.center_x = wall
            middle_wall_connector_sprite.center_y = 590
            # fence_list adds sprite to the fence_list
            self.fence_list.append(middle_wall_connector_sprite)
        # instance creation
        left_wall_corner_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0102.png", SPRITE_FENCE_SCALING)
        # position
        left_wall_corner_sprite.center_x = 15
        left_wall_corner_sprite.center_y = 10
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_wall_corner_sprite)
        # instance creation
        right_wall_corner_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0102.png", SPRITE_FENCE_SCALING)
        # position
        right_wall_corner_sprite.center_x = 790
        right_wall_corner_sprite.center_y = 10
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_wall_corner_sprite)
        for wall in range(20, 795, 5):
            # instance creation
            middle_wall_connector_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0100.png",
                                                SPRITE_FENCE_SCALING)
            # position
            middle_wall_connector_sprite.center_x = wall
            middle_wall_connector_sprite.center_y = 10
            # fence_list adds sprite to the fence_list
            self.fence_list.append(middle_wall_connector_sprite)
        for wall in range(20, 590, 10):
            # instance creation
            middle_upward_wall_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0123.png", 0.62)
            # position
            middle_upward_wall_sprite.center_x = 12
            middle_upward_wall_sprite.center_y = wall
            # fence_list adds sprite to the fence_list
            self.fence_list.append(middle_upward_wall_sprite)
        for wall in range(12, 590, 10):
            # instance creation
            middle_upward_wall_sprite = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0124.png", 0.62)
            # position
            middle_upward_wall_sprite.center_x = 793
            middle_upward_wall_sprite.center_y = wall
            # fence_list adds sprite to the fence_list
            self.fence_list.append(middle_upward_wall_sprite)
        # instance creation
        left_wall_corner_sprite1 = Wall("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0096.png", SPRITE_FENCE_SCALING)
        # position
        left_wall_corner_sprite1.center_x = 15
        left_wall_corner_sprite1.center_y = 590
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_wall_corner_sprite1)
        # instance creation
        right_wall_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0098.png",
                                          SPRITE_FENCE_SCALING)
        # position
        right_wall_corner_sprite1.center_x = 790
        right_wall_corner_sprite1.center_y = 590
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_wall_corner_sprite1)

        """fences around house"""
        for fence in range(300, 500, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 300
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(100, 150, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = fence
            middle_upward_fence_sprite.center_y = 300
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(250, 300, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = fence
            middle_upward_fence_sprite.center_y = 300
            self.fence_list.append(middle_upward_fence_sprite)
        # instance creation
        end_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0080.png", SPRITE_FENCE_SCALING)
        end_fence_sprite.center_x = 235
        end_fence_sprite.center_y = 300
        self.fence_list.append(end_fence_sprite)
        # instance creation
        end_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0082.png", SPRITE_FENCE_SCALING)
        end_fence_sprite.center_x = 155
        end_fence_sprite.center_y = 300
        self.fence_list.append(end_fence_sprite)
        # instance creation
        end_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0080.png", SPRITE_FENCE_SCALING)
        end_fence_sprite.center_x = 288
        end_fence_sprite.center_y = 100
        self.fence_list.append(end_fence_sprite)
        # instance creation
        end_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0082.png", SPRITE_FENCE_SCALING)
        end_fence_sprite.center_x = 102
        end_fence_sprite.center_y = 100
        self.fence_list.append(end_fence_sprite)
        for fence in range(100, 300, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0045.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = fence
            middle_upward_fence_sprite.center_y = 500
            self.fence_list.append(middle_upward_fence_sprite)
        # instance creation
        right_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0046.png",
                                           SPRITE_FENCE_SCALING)
        # position
        right_fence_corner_sprite1.center_x = 300
        right_fence_corner_sprite1.center_y = 500
        self.fence_list.append(right_fence_corner_sprite1)
        for fence in range(100, 500, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 300
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(100, 500, 10):
            # instance creation
            middle_upward_fence_sprite = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0071.png",
                                               SPRITE_FENCE_SCALING)
            # position
            middle_upward_fence_sprite.center_x = 90
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        # instance creation
        left_fence_corner_sprite1 = Fence("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0044.png",
                                          SPRITE_FENCE_SCALING)
        # position
        left_fence_corner_sprite1.center_x = 90
        left_fence_corner_sprite1.center_y = 500
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite1)

        """creates house in window"""
        wall_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0072.png", SPRITE_PLAYER_SCALING)
        wall_sprite.center_x = 130
        wall_sprite.center_y = 406
        self.house_list.append(wall_sprite)
        wall_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0085.png", SPRITE_PLAYER_SCALING)
        wall_sprite.center_x = 161
        wall_sprite.center_y = 406
        self.house_list.append(wall_sprite)
        wall_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0073.png", SPRITE_PLAYER_SCALING)
        wall_sprite.center_x = 138
        wall_sprite.center_y = 406
        self.house_list.append(wall_sprite)
        wall_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0073.png", SPRITE_PLAYER_SCALING)
        wall_sprite.center_x = 185
        wall_sprite.center_y = 406
        self.house_list.append(wall_sprite)
        wall_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0075.png", SPRITE_PLAYER_SCALING)
        wall_sprite.center_x = 201
        wall_sprite.center_y = 406
        self.house_list.append(wall_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0048.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 130
        roof_sprite.center_y = 450
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0049.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 151
        roof_sprite.center_y = 450
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0050.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 171
        roof_sprite.center_y = 450
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0051.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 181
        roof_sprite.center_y = 450
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0050.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 201
        roof_sprite.center_y = 450
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0060.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 130
        roof_sprite.center_y = 430
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0060.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 181
        roof_sprite.center_y = 430
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0062.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 141
        roof_sprite.center_y = 430
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0063.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 161
        roof_sprite.center_y = 430
        self.house_list.append(roof_sprite)
        roof_sprite = House("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0062.png", SPRITE_PLAYER_SCALING)
        roof_sprite.center_x = 201
        roof_sprite.center_y = 430
        self.house_list.append(roof_sprite)

        """"creates grass in the window"""
        for row in range(0, SCREEN_WIDTH + 10, 5):
            for column in range(0, SCREEN_HEIGHT, 5):
                # instance creation
                grass_sprite = Grass("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0001.png", SPRITE_GRASS_SCALING)
                grass_sprite.center_x = row
                grass_sprite.center_y = column
                self.grass_list.append(grass_sprite)
        """creates flower grass in the window"""
        for row in range(0, 100, 5):
            for column in range(0, 150, 5):
                # instance creation
                grass_sprite = Grass("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0002.png", SPRITE_GRASS_SCALING)
                grass_sprite.center_x = random.randint(20, SCREEN_WIDTH - 20)
                grass_sprite.center_y = random.randint(20, SCREEN_HEIGHT - 20)
                self.grass_list.append(grass_sprite)
        """creates gravel path"""
        for path in range(360, 390, 20):
            # instance creation
            gravel_sprite = Grass("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0043.png", SPRITE_GRASS_SCALING + 1)
            gravel_sprite.center_x = 160
            gravel_sprite.center_y = path
            self.grass_list.append(gravel_sprite)
        """creates trees and checks for collisions"""
        for row in range(TREE_COUNT):
            tree_place_success = False
            while not tree_place_success:
                # instance creation
                tree_sprite = Grass("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0004.png", SPRITE_GRASS_SCALING)
                tree_sprite.center_x = random.randrange(100, SCREEN_WIDTH)
                tree_sprite.center_y = random.randrange(540)
                tree_sprite1 = Grass("Lab 9 - Resources/kenney_tiny-town/Tiles/tile_0016.png", SPRITE_GRASS_SCALING)
                tree_sprite1.center_x = tree_sprite.center_x
                tree_sprite1.center_y = tree_sprite.center_y - 10
                # collision checks
                tree_hit_list = arcade.check_for_collision_with_list(tree_sprite, self.fence_list)
                tree_hit_list1 = arcade.check_for_collision_with_list(tree_sprite1, self.fence_list)
                tree_hit_list2 = arcade.check_for_collision_with_list(tree_sprite, self.tree_list)
                tree_hit_list3 = arcade.check_for_collision_with_list(tree_sprite1, self.tree_list)
                house_hit_tree_list = arcade.check_for_collision_with_list(tree_sprite, self.house_list)
                house_hit_tree_list1 = arcade.check_for_collision_with_list(tree_sprite1, self.house_list)
                if len(tree_hit_list) == 0 and len(tree_hit_list1) == 0 and len(house_hit_tree_list) == 0 and len(
                        house_hit_tree_list1) == 0 and len(tree_hit_list2) == 0 and len(tree_hit_list3) == 0:
                    tree_place_success = True
                    self.tree_list.append(tree_sprite)
                    self.tree_list.append(tree_sprite1)

        # variable that defines the image of the player, instance creation
        self.player_sprite = Player("Lab 9 - Resources/kenney_tiny-dungeon/Tiles/tile_0085.png", SPRITE_PLAYER_SCALING)
        # position
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 200
        # player_list adds the player_sprite to the player_list
        self.player_list.append(self.player_sprite)
        # variable that defines the image of the npc, instance creation
        crab_sprite = Crab("Lab 9 - Resources/kenney_tiny-dungeon/Tiles/tile_0110.png", SPRITE_PLAYER_SCALING - 0.5)
        # position
        crab_sprite.center_x = 440
        crab_sprite.center_y = 440
        crab_sprite.change_x += 0.3
        # player_list adds the npc_sprite to the npc_list
        self.npc_list.append(crab_sprite)

        # physics_engine will stop sprites from moving into object
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.fence_list)
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.player_sprite, self.house_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.player_sprite, self.tree_list)
        self.physics_engine3 = arcade.PhysicsEngineSimple(crab_sprite, self.tree_list)
        self.physics_engine4 = arcade.PhysicsEngineSimple(crab_sprite, self.fence_list)

    # when key is pressed, method in MyGame class
    def on_key_press(self, key: int, modifiers: int):
        # condition
        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    # when key is released, method in MyGame class
    def on_key_release(self, key: int, modifiers: int):
        # condition
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

    # method in MyGame that will draw what is defined in the list
    def on_draw(self):
        arcade.start_render()
        # clears on_draw
        self.clear()
        # selects the camera to use for player sprite
        self.camera_sprite.use()
        # draws all sprites
        self.grass_list.draw()
        self.coin_list.draw()
        self.fence_list.draw()
        self.player_list.draw()
        self.npc_list.draw()
        self.house_list.draw()
        self.tree_list.draw()
        # selects the camera to use for score
        self.camera_gui.use()
        # creates score board
        result = f" Score: {self.score}"
        arcade.draw_text(self.score, 750, 550, arcade.color.WHITE, 20, 5)
        arcade.set_background_color((20, 20, 30))

    # method in the MyGame class that will update lists
    def on_update(self, delta_time: float):
        self.player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # condition
        for coin in self.player_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.coin_sound_player = arcade.play_sound(coin_sound, volume=0.3)
        self.player_hit_list2 = arcade.check_for_collision_with_list(self.player_sprite, self.fence_list)
        for hit in self.player_hit_list2:
            if not self.bump_sound_player or not self.bump_sound_player.playing:
                self.bump_sound_player = arcade.play_sound(bump_sound, volume=1,)
        # condition
        for crab in self.npc_list:
            # makes crab follow player
            crab.follow_sprite(self.player_sprite)
        # updates list
        self.coin_list.update()
        self.tree_list.update()
        self.house_list.update()
        # updates the physics_engine
        self.physics_engine.update()
        self.physics_engine1.update()
        self.physics_engine2.update()
        self.physics_engine3.update()
        self.physics_engine4.update()
        # scrolls screen to player
        self.scroll_to_player()

    def scroll_to_player(self):
        # based on where the player is, the camera will position to be centered on player
        # so window width is 800, player is at 100, 800/2 = 400, 100 - 400 = -300, so camera will start at -300
        position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
        # camera will move to position at set speed
        self.camera_sprite.move_to(position, CAMERA_SPEED)

    def on_resize(self, width: float, height: float):
        # resizes the window when player hits edge
        self.camera_sprite.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()

