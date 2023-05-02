import arcade
class Game(arcade.Window):
    def __init__(self):
        super().__init__(400, 300, 'Sound demo')
        self.text = 'stop'
        self.music = arcade.load_sound(':resources:music/funkyrobot.mp3')
        self.media_player = self.music.play()
class Song:
    def __init__(self):
        self.exploration = arcade.load_sound('DS1_Char_Creation.mp3')
        self.exploration_player = None

if not self.exploration_player or not self.exploration_player.playing:
    exploration_player = arcade.play_sound(self.exploration)