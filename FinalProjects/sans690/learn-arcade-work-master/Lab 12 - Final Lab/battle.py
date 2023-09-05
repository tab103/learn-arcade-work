import time
import pygame
import arcade
from setup_function import theme_song_player
import random
from part_12 import Monster, MyGame

# dirty sprite code by Professor Gerry Jenkins on YouTube and gerryjenkinslb on GitHub and
# https://github.com/gerryjenkinslb/pygame_dirtysprites

battle = True
if battle:
    # music credit to Nintendo and GameFreak
    sound_file = "Sound Resources/Assets_Sounds_Music_battle (vs trainer).wav"
    battle_sound = arcade.load_sound(sound_file, streaming=True)

win_size = (800, 600)  # you may need to adjust this for windows, linux


class Player(pygame.sprite.DirtySprite):  # our DirtySprite class

    def __init__(self, center, dx, dy):
        pygame.sprite.DirtySprite.__init__(self)  # always need to have this call to super constructor
        # Credit for image: PKMNTrainerRick on Deviant Art
        # https://www.deviantart.com/pkmntrainerrick/art/POKEMON-HILBERT-SPRITES-914974956
        # Also credit to Nintendo and GameFreak for original concept
        self.image = pygame.image.load("Player Resources/pngs/HilbertBack1.png")
        self.rect = self.image.get_rect(center=center)  # rect controls target place when copied to screen
        self.dx, self.dy = dx, dy  # change to move every frame

    def update(self):  # make changes for this time tick
        x, y = self.rect.center  # move current center
        # changing number makes it move all over screen
        x = (x / 10 + self.dx) % win_size[0] - 630  # move by dx,dy and wrap modulo window size
        y = 368.9
        self.rect.center = (x, y)  # changes where sprite will be copied to buffer
        self.dirty = 1  # force redraw from image, since we moved the sprite rect


class NPC(pygame.sprite.DirtySprite):  # our DirtySprite class

    def __init__(self, center, dx, dy):
        pygame.sprite.DirtySprite.__init__(self)  # always need to have this call to super constructor

        # Credit for image: Othienka on Deviant Art
        # https://www.deviantart.com/othienka/art/Team-Rocket-Player-Character-595571094
        # Also credit to Nintendo and GameFreak for original concept
        self.image = pygame.image.load("Player Resources/pngs/TeamRocketGruntBackGen4.png")
        self.rect = self.image.get_rect(center=center)  # rect controls target place when copied to screen
        self.dx, self.dy = dx, dy  # change to move every frame

    def update(self):  # make changes for this time tick
        x, y = self.rect.center  # move current center
        # changing number makes it move all over screen
        x = (x / 6 + self.dx) % win_size[0] - 150  # move by dx,dy and wrap modulo window size
        y = 230
        self.rect.center = (x, y)  # changes where sprite will be copied to buffer
        self.dirty = 1  # force redraw from image, since we moved the sprite rect


class Pokemon0(pygame.sprite.DirtySprite):  # our DirtySprite class

    def __init__(self, center, dx, dy):
        pygame.sprite.DirtySprite.__init__(self)  # always need to have this call to super constructor
        # credit to Nintendo and GameFreak for original concept
        self.image = pygame.image.load("Pokemon Resources/pngs/Bal.png")
        self.rect = self.image.get_rect(center=center)  # rect controls target place when copied to screen
        self.dx, self.dy = dx, dy  # change to move every frame

    def update(self):  # make changes for this time tick
        x, y = self.rect.center  # move current center
        # changing number makes it move all over screen
        x = (x / 9 + self.dx) % win_size[0] - 400  # move by dx,dy and wrap modulo window size
        y = 420
        self.rect.center = (x, y)  # changes where sprite will be copied to buffer
        self.dirty = 1  # force redraw from image, since we moved the sprite rect


class Pokemon1(pygame.sprite.DirtySprite):  # our DirtySprite class

    def __init__(self, center, dx, dy):
        pygame.sprite.DirtySprite.__init__(self)  # always need to have this call to super constructor
        # credit to Nintendo and GameFreak for original concept
        self.image = pygame.image.load("Pokemon Resources/pngs/Bal2.png")
        self.rect = self.image.get_rect(center=center)  # rect controls target place when copied to screen
        self.dx, self.dy = dx, dy  # change to move every frame

    def update(self):  # make changes for this time tick
        x, y = self.rect.center  # move current center
        # changing number makes it move all over screen
        x = (x / 9 + self.dx) % win_size[0] - 210  # move by dx,dy and wrap modulo window size
        y = 280
        self.rect.center = (x, y)  # changes where sprite will be copied to buffer
        self.dirty = 1  # force redraw from image, since we moved the sprite rect


def is_exit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def main(self=Player):
    # Initialize Everything
    pygame.init()
    draw_buffer = pygame.display.set_mode(win_size)
    pygame.display.set_caption('Battle')
    font = pygame.font.Font("Interface Resources/Orange kid.ttf", 25)
    user_pokemon_name = "Bulbasaur"
    foe_pokemon_name = "Bulbasaur"
    user_pokemon_lvl = "10"
    foe_pokemon_lvl = "11"
    battle_sound_player = None

    # Create The Background used to restore sprite previous location
    screen = pygame.Surface(draw_buffer.get_size())  # make a surface the size of display area
    # Images compiled on The Sprite Resource, credit to Nintendo and GameFreak
    # https: // www.spriters - resource.com / ds_dsi / pokemonplatinum / sheet / 18502 /
    # https: // www.spriters - resource.com / ds_dsi / pokemonheartgoldsoulsilver / sheet / 26753 /
    screen.blit(pygame.image.load("Battle Resources/pngs/Battle Backgrounds(edited).png"),
                (0, 0))  # draw image into sprite surface
    # Prepare Game Objects
    clock = pygame.time.Clock()  # Clock is object that will allow fairly exact frame rate

    cx, cy = win_size[0] // 2, win_size[1] // 2  # figure out middle of display area

    pok0 = Pokemon0((0, 0), -120, 0)
    pok1 = Pokemon1((0, 0), -120, 0)
    npc = NPC((0, 0), -120, 0)
    player = Player((0, 0), -20, 0)  # add face 0 5000 down and to right from center -20 0 is movement
    my_sprites = pygame.sprite.LayeredDirty(player, npc, pok0, pok1)  # holds sprites to be drawn
    my_sprites.add(player, npc, pok0, pok1)  # add to our group
    my_sprites.clear(draw_buffer, screen)  # copy background to screen

    # music credit to Nintendo and GameFreak
    if not battle_sound_player or not battle_sound_player.playing:
        battle_sound_player = arcade.play_sound(battle_sound, looping=True, volume=10)
        if battle_sound_player:
            arcade.stop_sound(theme_song_player)

    # Image compiled on The Sprite Resource, credit to Nintendo and GameFreak
    # https: // www.spriters - resource.com / ds_dsi / pokemonheartgoldsoulsilver / sheet / 30540 /
    # npc_health bar
    foe_healthbar_image = pygame.image.load("Battle Resources/pngs/foehealthbar.png")
    screen.blit(foe_healthbar_image, (-15, 50))

    # Image compiled on The Sprite Resource, credit to Nintendo and GameFreak
    #  https: // www.spriters - resource.com / ds_dsi / pokemonheartgoldsoulsilver / sheet / 30540 /
    # player health bar
    player_healthbar_image = pygame.image.load("Battle Resources/pngs/playerhealthbar.png")
    screen.blit(player_healthbar_image, (500, 330))

    while True:
        text_surface = [font.render(user_pokemon_name, True, (0, 0, 0)), font.render(foe_pokemon_name, True, (0, 0, 0)),
                        font.render(user_pokemon_lvl, True, (0, 0, 0)), font.render(foe_pokemon_lvl, True, (0, 0, 0))]
        if is_exit_event():
            break  # break out of loop and exit
        my_sprites.update()  # call update on all sprites

        # for each dirty sprint, erase previous rect with background copy
        # and then copy new sprite to buffer
        rects = my_sprites.draw(draw_buffer)

        clock.tick(10)  # times per second, delays for the time till next frame point

        draw_buffer.blit(text_surface[0], (10, 85)) and draw_buffer.blit(text_surface[1], (555, 360)), draw_buffer.blit(
            text_surface[2], (755, 360)), draw_buffer.blit(text_surface[3], (200, 85))

        pygame.display.update()

        # --- classes --- (CamelCase names)

        # empty

        # --- functions --- (lower_case names)
    game_display_rect = draw_buffer.get_rect()

    def button_check(button):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if button['rect'].collidepoint(mouse):
            if click[0] == 1 and button['action']:
                button['action']()

    def button_draw(button):

        mouse = pygame.mouse.get_pos()

        if button['rect'].collidepoint(mouse):
            color = button['ac']
        else:
            color = button['ic']

        pygame.draw.rect(draw_buffer, color, button['rect'])

        image, rect = text_objects(button['msg'], font)
        rect.center = button['rect'].center
        draw_buffer.blit(image, rect)

    def text_objects(text, font):
        image = font.render(text, True, "Black")
        rect = image.get_rect()
        return image, rect

    def message_display(text):
        image, rect = text_objects(text, font)
        rect.center = game_display_rect.center
        draw_buffer.blit(image, rect)
        pygame.display.update()

    def game_intro():

        image, rect = text_objects("", font)
        rect.center = game_display_rect.center
        draw_buffer.blit(image, rect)

        image, rect = text_objects("", font)
        rect.center = game_display_rect.center
        draw_buffer.blit(image, rect)

        buttons = [
            {
                'msg': 'Attack',
                'rect': pygame.Rect(30, 480, 100, 50),
                'ac': "White",
                'ic': "White",
                'action': game_loop,
            },
            {
                'msg': 'Run',
                'rect': pygame.Rect(360, 480, 100, 50),
                'ac': "White",
                'ic': "White",
                'action': game_loop2,
            }
        ]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_check(buttons[0])
                    button_check(buttons[1])

            button_draw(buttons[0])
            button_draw(buttons[1])
            pygame.display.update()

    def game_loop():

        image, rect = text_objects("", font)

        rect.center = (game_display_rect.centerx, 100)
        draw_buffer.blit(image, rect)

        buttons = [
            {
                'msg': 'Tackle',
                'rect': pygame.Rect(30, 480, 100, 50),
                'ac': "White",
                'ic': "White",
                'action': option2_loop
            }
        ]
        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_check(buttons[0])

            button_draw(buttons[0])
            pygame.display.update()

    def option2_loop():
        image, rect = text_objects("", font)
        rect.center = (game_display_rect.centerx, 100)
        draw_buffer.blit(image, rect)

        num = random.randint(10, 20)
        self.enemy_damage += self.num
        self.pokemon_health -= self.enemy_damage
        self.pokemon_damage += self.num
        self.enemy_health -= self.pokemon_damage

        text_line0 = "Effective."
        if text_line0:
            print(f'Enemy pokemon is at {self.enemy_health} health.')
            self.enemy_health = self.enemy_health - self.pokemon_damage
            if self.enemy_health < 0:
                print("Your opponent was defeated!")
            return
        text_line1 = "Ineffective."
        print("Move missed!")

        lines = [text_line0, text_line1]

        buttons = [
            {
                'msg': text_line0 or text_line1,
                'rect': pygame.Rect(30, 480, 100, 50),
                'ac': "White",
                'ic': "White",
                'action': game_intro()
            }
        ]
        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_check(buttons[0])
                    button_check(buttons[1])
            button_draw(buttons[0])
            button_draw(buttons[1])
            pygame.display.update()

    def game_loop2():

        image, rect = text_objects("", font)
        rect.center = (game_display_rect.centerx, 100)
        draw_buffer.blit(image, rect)

        text_line2 = "No escape."
        buttons = [
            {
                'msg': text_line2,
                'rect': pygame.Rect(360, 480, 100, 50),
                'ac': "White",
                'ic': "White",
                'action': game_intro
            }
        ]

        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_check(buttons[0])

            button_draw(buttons[0])
            pygame.display.update()

            # --- main ---

    pygame.init()

    game_display_rect = draw_buffer.get_rect()

    game_intro()


if __name__ == '__main__':
    main()
