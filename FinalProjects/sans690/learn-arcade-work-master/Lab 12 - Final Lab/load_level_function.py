import arcade

# --Constant--
MAP_SCALING = 1.5


# Credit for tiles used in tilemaps: ChaoticCherryCake and Akizakura16
# https://www.deviantart.com/chaoticcherrycake/art/Public-Indoor-Tileset-From-Public-Tiles-483814875
# https://www.deviantart.com/akizakura16/art/4th-gen-Indoor-Tileset-624832808
# https://www.deviantart.com/akizakura16/art/4th-gen-Outdoor-Tileset-613857695
# Also credit to Nintendo and GameFreak for original concept

def load_level(self):
    # Bedroom
    if self.current_room == 0:
        resource = "Inside Resources/Gen4Bedroom.tmj"
        objects = "Objects"
        tables = "Tables"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING, hit_box_algorithm="None")
        list_of_lists = [self.tile_map.sprite_lists[f"{objects}"], self.tile_map.sprite_lists[f"{tables}"]]
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, list_of_lists)

    # Downstairs
    elif self.current_room == 1:
        resource = "Inside Resources/Gen4Kitchen.tmj"
        objects = "Objects"
        tables = "Tables"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING, hit_box_algorithm="None")
        list_of_list = [self.tile_map.sprite_lists[f"{tables}"], self.tile_map.sprite_lists[f"{objects}"]]
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, list_of_list)

    # Outside
    elif self.current_room == 2:
        resource = "Outside Resources/Version 3/OutsideTilemap.tmj"
        fence = "Fence"
        trees00 = "Trees"
        trees01 = "Trees(with collision)"
        buildings = "Buildings"
        objects = "Objects"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING, hit_box_algorithm="None")
        list_of_list = [self.tile_map.sprite_lists[f"{fence}"], self.tile_map.sprite_lists[f"{trees00}"],
                        self.tile_map.sprite_lists[f"{trees01}"], self.tile_map.sprite_lists[f"{buildings}"],
                        self.tile_map.sprite_lists[f"{objects}"]]
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, list_of_list)
    # Wild
    elif self.current_room == 3:
        resource = "Outside Resources/Version 2/WildGen4Tilemap.tmj"
        fence = "Fence"
        trees00 = "Trees"
        trees01 = "Trees(with collision)"
        objects = "Objects"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING, hit_box_algorithm="None")
        list_of_lists = [self.tile_map.sprite_lists[f"{fence}"], self.tile_map.sprite_lists[f"{trees00}"],
                         self.tile_map.sprite_lists[f"{trees01}"], self.tile_map.sprite_lists[f"{objects}"]]
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, list_of_lists)

    # Forest
    elif self.current_room == 4:
        resource = "Outside Resources/Version 3/BorderForestGen4Tilemap.tmj"
        fence = "Fence"
        trees00 = "Trees"
        trees01 = "Trees(with collision)"
        objects = "Objects"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING, hit_box_algorithm="None")
        list_of_lists = [self.tile_map.sprite_lists[f"{fence}"], self.tile_map.sprite_lists[f"{trees00}"],
                         self.tile_map.sprite_lists[f"{trees01}"], self.tile_map.sprite_lists[f"{objects}"]]
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, list_of_lists)
