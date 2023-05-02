from load_level_function import load_level
import arcade

# music credit to Nintendo and GameFreak
sound_file = "Sound Resources/Pallet Town Theme.wav"
theme_song = arcade.load_sound(sound_file, True)
theme_song_player = arcade.play_sound(theme_song, volume=30, looping=True)


def enemy_here(self):
    self.npc_sprite.center_x = 660
    self.npc_sprite.center_y = 360
    image_location_list = [[0, 0, 300, 300]]
    # Credit for image: Othienka on Deviant Art,
    # https://www.deviantart.com/othienka/art/Team-Rocket-Player-Character-595571094
    # Also credit to Nintendo and GameFreak for original concept
    file_name = "Player Resources/pngs/TeamRocketGruntGen4.png"
    self.npc_sprite.stand_right_textures = \
        arcade.load_textures(file_name, image_location_list, False, hit_box_algorithm="Detailed")


def setup_game(self):
    # condition
    # if the current room is 0, then do this code
    if self.current_room == 0:
        load_level(self)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 150

    # condition
    # if the current room is 1, then do this code
    elif self.current_room == 1:
        load_level(self)
        self.player_sprite.center_x = 668
        self.player_sprite.center_y = 220

    # condition
    # if the current room is 2, then do this code
    elif self.current_room == 2:
        load_level(self)
        self.player_sprite.center_x = 700
        self.player_sprite.center_y = 700

    # condition
    # if the current room is 3, then do this code
    elif self.current_room == 3:
        load_level(self)
        self.player_sprite.center_x = 965
        self.player_sprite.center_y = 40
        enemy_here(self)

    # condition
    # if the current room is 4, then do this code
    elif self.current_room == 4:
        load_level(self)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 170
        enemy_here(self)
        
