import time
import pygame
from dialogue import text, options, attack_options, bag_options, run_option, pokemon_option
import arcade
from setup_function import theme_song_player
import random
import part_12

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
        battle_sound_player = arcade.play_sound(battle_sound, looping=True)
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

        draw_buffer.blit(text_surface[0], (10, 85)) and draw_buffer.blit(text_surface[1], (555, 350)), draw_buffer.blit(
            text_surface[2], (755, 360)), draw_buffer.blit(text_surface[3], (200, 85))

        pygame.display.update()
        text_line = "A foe wants to battle!"
        text_surface = font.render(text_line, True, (0, 0, 0))
        draw_buffer.blit(text_surface, (40, 470))
        delay = 100
        pygame.time.delay(delay)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                text()

                delay = 600
                pygame.time.delay(delay)
                draw_buffer.blit(screen, (0, 0))
                options()

        #  if event.type == pygame.MOUSEBUTTONDOWN:
        # screen.fill("white")
        # draw_buffer.fill("white")
        #  time.sleep(0)
        #  pygame.display.update()  # copy rects from buffer to screen


if __name__ == '__main__':
    main()

    """next_turn = 0
    player_turn = next_turn == 0
    foe_turn = next_turn == 1
    if player_turn:
        for event in pygame.event.get():
            if event.type == pygame.K_a:
                attack_options()
                pygame.display.update()
                pygame.time.delay(delay)
                draw_buffer.blit(screen, (0, 0))

              if key == arcade.key.A:
                attack_options()
                if key == arcade.key.T:
                    for i in range(2):
                        if i == 0:
                            text_line2 = "It was effective."
                            text2 = font.render(text_line2, True, (0, 0, 0))
                            draw_buffer.blit(text2, (40, 470))
                            damage = 100
                            Player.pokemon_health = Player.pokemon_health
                            for i in range(damage):
                                damage_to_pokemon = Player.pokemon_health - i
                                Player.pokemon_health -= damage_to_pokemon
                                player_turn + 1
                        elif i == 1:
                            text_line3 = "It was not effective."
                            text3 = font.render(text_line3, True, (0, 0, 0))
                            draw_buffer.blit(text3, (40, 470))
                            Player.pokemon_health = Player.pokemon_health
                            player_turn + 1
            elif key == arcade.key.B:
                bag_options()
            elif key == arcade.key.P:
                pokemon_option()
            elif key == arcade.key.R:
                run_option()
        next_turn = player_turn + 1

    elif foe_turn:
        for i in range(2):
            if i == 0:
                text_line2 = "Foe uses tackle, it was effective."
                text2 = font.render(text_line2, True, (0, 0, 0))
                draw_buffer.blit(text2, (40, 470))
                damage = 100
                NPC.pokemon_health = NPC.pokemon_health
                for i in range(damage):
                    damage_to_pokemon = NPC.pokemon_health - i
                    NPC.pokemon_health -= damage_to_pokemon
                    next_turn = foe_turn - 1
            elif i == 1:
                text_line3 = "Foe uses tackle, it was not effective."
                text3 = font.render(text_line3, True, (0, 0, 0))
                draw_buffer.blit(text3, (40, 470))
                NPC.pokemon_health = NPC.pokemon_health
                next_turn = foe_turn - 1
        if Player.pokemon_health or NPC.pokemon_health == 100:
            battle = False
            pygame.display.quit()"""
