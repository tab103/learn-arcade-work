import battle
import load_level_function
import logging
from part_12 import PLAYER_MOVEMENT_SPEED
import arcade
from setup_function import enemy_here
import time


def update(self):
    self.player_sprite_list.update()
    self.player_sprite_list.update_animation()
    self.npc_sprite_list.update()
    self.npc_sprite_list.update_animation()

    # scrolls screen to player
    self.scroll_to_player()
    if self.current_room == 0 or self.current_room == 1:
        self.physics_engine.update()
    elif self.current_room == 2:
        self.physics_engine.update()
    elif self.current_room == 3:
        self.physics_engine.update()
    elif self.current_room == 4:
        self.physics_engine.update()

    # condition
    # if the current room is 0, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    if self.current_room == 0:
        if self.player_sprite.center_x > 455:
            self.player_sprite.center_x = 455
        elif self.player_sprite.center_x < 30:
            self.player_sprite.center_x = 30
        elif self.player_sprite.center_y > 250:
            self.player_sprite.center_y = 250
        elif self.player_sprite.center_y < 30:
            self.player_sprite.center_y = 30
        while self.player_sprite.center_y >= 175 and self.player_sprite.center_y <= 250 \
                and self.player_sprite.center_x >= 380 and self.current_room == 0:
            logging.warn("Moved to kitchen.")
            # moves to kitchen
            self.current_room += 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 665
            self.player_sprite.center_y = 220
            enemy_here(self)

    # condition
    # if the current room is 1, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    elif self.current_room == 1:
        if self.player_sprite.center_x > 690:
            self.player_sprite.center_x = 690
        elif self.player_sprite.center_x < 30:
            self.player_sprite.center_x = 30
        elif self.player_sprite.center_y > 265:
            self.player_sprite.center_y = 265
        elif self.player_sprite.center_y < 30:
            self.player_sprite.center_y = 30
        while self.player_sprite.center_y >= 220 and self.player_sprite.center_x <= 660 and \
                self.current_room == 1 and self.player_sprite.center_y <= 270 and self.player_sprite.center_x >= 620:
            logging.warn("Moved back to bedroom.")
            # moves back to bedroom
            self.current_room -= 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 370
            self.player_sprite.center_y = 200

        while self.player_sprite.center_y <= 30 and self.player_sprite.center_x >= 300 and self.current_room == 1 \
                and self.player_sprite.center_x <= 380:
            logging.warn("Moved to outside.")
            # moves outside
            self.current_room += 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 700
            self.player_sprite.center_y = 705
            enemy_here(self)

    # condition
    # if the current room is 2, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    elif self.current_room == 2:
        if self.player_sprite.center_x > 930:
            self.player_sprite.center_x = 930
        elif self.player_sprite.center_x < 30:
            self.player_sprite.center_x = 30
        elif self.player_sprite.center_y > 930:
            self.player_sprite.center_y = 930
        elif self.player_sprite.center_y < 80:
            self.player_sprite.center_y = 80
        while self.player_sprite.center_y >= 660 and self.player_sprite.center_y <= 665 and self.player_sprite.center_x <= 690 and self.player_sprite.center_x >= 630 and self.current_room == 2:
            logging.warn("Moved back to kitchen.")
            # moves back to kitchen
            self.current_room -= 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 340
            self.player_sprite.center_y = 35
        # the center_x might need to be changed due to invisible boxes in the way
        while self.player_sprite.center_y >= 930 and self.player_sprite.center_y <= 970 and self.current_room == 2 and self.player_sprite.center_x >= 360:
            logging.warn("Moved to wild.")
            # moves to wild
            self.current_room += 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 965
            self.player_sprite.center_y = 40
            enemy_here(self)

    # condition
    # if the current room is 3, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    elif self.current_room == 3:
        if self.player_sprite.center_x <= 684 and self.player_sprite.center_x >= 665 and self.player_sprite.center_y <= 400:
            self.player_sprite.center_x = 682
            self.player_sprite.change_y = 0
            self.player_sprite.change_x = 0
            self.npc_sprite.change_y = -10
            npc_hit_player_list = []
            npc_hit_player = arcade.check_for_collision_with_list(self.player_sprite, self.npc_sprite_list)
            npc_hit_player_list.append(npc_hit_player)
            if len(npc_hit_player_list) > 0:
                self.npc_sprite.center_y = self.player_sprite.center_y + 70 - PLAYER_MOVEMENT_SPEED
                time.sleep(0.2)
            battle.main(self)
        if self.player_sprite.center_x > 1900:
            self.player_sprite.center_x = 1900
        elif self.player_sprite.center_x < 30:
            self.player_sprite.center_x = 30
        elif self.player_sprite.center_y < 30:
            self.player_sprite.center_y = 30
        elif self.player_sprite.center_y > 950:
            self.player_sprite.center_y = 950
        while self.player_sprite.center_y >= 830 and self.player_sprite.center_y <= 840 and self.player_sprite.center_x >= 200 and self.player_sprite.center_x <= 400 and self.current_room == 3:
            logging.warn("Moved to forest.")
            # moves to forest
            self.current_room += 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 240
            self.player_sprite.center_y = 160
        while self.player_sprite.center_y <= 35 and self.player_sprite.center_x <= 1010 and self.player_sprite.center_x >= 900 and self.current_room == 3:
            logging.warn("Moved back to outside.")
            # moves back to outside
            self.current_room -= 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 490
            self.player_sprite.center_y = 930
            enemy_here(self)

    # condition
    # if the current room is 4, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    elif self.current_room == 4:
        if self.player_sprite.center_x > 470:
            self.player_sprite.center_x = 470
        elif self.player_sprite.center_x < 10:
            self.player_sprite.center_x = 10
        elif self.player_sprite.center_y < 10:
            self.player_sprite.center_y = 10
        elif self.player_sprite.center_y > 710:
            self.player_sprite.center_y = 710
        while self.player_sprite.center_y <= 158 and self.current_room == 4:
            logging.warn("Moved to wild.")
            # moves back to wild
            self.current_room -= 1
            load_level_function.load_level(self)
            self.player_sprite.center_x = 320
            self.player_sprite.center_y = 825
            enemy_here(self)
            
