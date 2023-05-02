import pygame

win_size = (800, 600)
draw_buffer = pygame.display.set_mode(win_size)
pygame.font.init()
font = pygame.font.Font("Interface Resources/Orange kid.ttf", 25)


def text():
    text_line = "A foe wants to battle!"
    text = font.render(text_line, True, (0, 0, 0))
    draw_buffer.blit(text, (40, 470))


def options():
    text1_line = "A. Attack"
    text2_line = "P. Pokemon"
    text3_line = "B. Bag"
    text4_line = "R. Run"

    text1 = font.render(text1_line, True, (0, 0, 0))
    text2 = font.render(text2_line, True, (0, 0, 0))
    text3 = font.render(text3_line, True, (0, 0, 0))
    text4 = font.render(text4_line, True, (0, 0, 0))

    draw_buffer.blit(text1, (50, 480))
    draw_buffer.blit(text2, (350, 480))
    draw_buffer.blit(text3, (50, 540))
    draw_buffer.blit(text4, (350, 540))


def attack_options():
    text_line0 = "T. Tackle"
    text0 = font.render(text_line0, True, (0, 0, 0))
    draw_buffer.blit(text0, (50, 480))

    #text_line1 = "Bulbasaur used tackle."
    #text1 = font.render(text_line1, True, (0, 0, 0))
   # draw_buffer.blit(text1, (50, 480))


def bag_options():
    text_line = "Nothing is in you bag."
    text = font.render(text_line, True, (0, 0, 0))
    draw_buffer.blit(text, (50, 480))


def run_option():
    text_line = "You can't escape!"
    text = font.render(text_line, True, (0, 0, 0))
    draw_buffer.blit(text, (50, 480))


def pokemon_option():
    text_line = "You have no other pokemon!"
    text = font.render(text_line, True, (0, 0, 0))
    draw_buffer.blit(text, (50, 480))
