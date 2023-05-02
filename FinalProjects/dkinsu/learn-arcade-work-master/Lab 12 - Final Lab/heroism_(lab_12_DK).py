import random
import arcade
import lab_12_models
import lab_12_rooms
import lab_12_items
import lab_12_combatants

# Inventory and out of play
INV = -1
OOP = -2

# Music
# Character creation theme from Dark Souls
exploration = arcade.load_sound('DS1_Char_Creation.mp3')
exploration_player = exploration.play(0.5, 0, True)

# Locked Girl - The Girl's Secret Room - From Touhou 6 EoSD
cube_fight = arcade.load_sound('Locked_Girl_TGSR.mp3')

# The Maid and the Pocket Watch of Blood - From Touhou 6 EoSD
long_fight = arcade.load_sound('mapwb.mp3')

# Septette for the Dead Princess - From Touhou 6 EoSD
dragon_fight = arcade.load_sound('Septette.mp3')

# Lunar Clock - Luna Dial - From Touhou 6 EoSD
fiend_fight = arcade.load_sound('Lunar_Clock_Luna_Dial.mp3')


def get_item(item_list, name):
    for item in item_list:
        if name == item.i_name:
            return item


def main():
    wizard = lab_12_combatants.PlayerClass("A class that wields magic.\nPowerful ranged offense, weaker defense.",
                                            "Wizard", 40, 40, 5, 60, 60, "Amplify", "Flare", 4,
                                            'Triples your attack power for the duration of the battle. '
                                            'Can be used multiple times. Costs 40 mana.',
                                            'Cause a fiery explosion. High damage. 4 range. Costs 20 mana.',
                                           'On battle victory, heals 5 HP and gains 5 max HP and 10 max mana.')

    warrior = lab_12_combatants.PlayerClass("A class that fights with heavy close ranged weapons."
                                            "\nClose-ranged offense, strong defense.",
                                            "Warrior", 60, 60, 8, 30, 30, "Invigorating Cleave", "Guard", 2,
                                            'A long-reaching (2) powerful swing. Deals extra damage proportional to '
                                            'warrior\'s missing HP, and returns 33% of warrior\'s missing HP. Costs 15 mana.',
                                            'Heavily reduces incoming damage. Requires 10 mana to use, but restores 10 mana.',
                                            'On battle victory, increases max HP by 10, heals for 66% of missing HP, and gains 1 attack.')

    rogue = lab_12_combatants.PlayerClass("A class that fights with melee and ranged weapons."
                                          "\nVersatile offense, middling defense.",
                                            'Rogue', 50, 50, 10, 45, 45, "Lacerate", "Retreating Shot", 1,
                                            'A devastating close-ranged attack. Incredible range (3), but leaves you close to the enemy.\n'
                                            ' heavy damage. Halves the damage of the next enemy attack. Costs 15 mana.',
                                            'Fire a shot with a bow before performing evasive maneuvers. '
                                            'Creates distance (2). 3 range. Costs 25 mana.',
                                          'On battle victory, gains 15 max mana and 3 attack.')

    cube = lab_12_combatants.Enemy('A BIG CUBE.', 'THE CUBE', 80, 'CUBIC CONTACT', 7,
                                   'CUBE HYPER STRIKE', 14, 'YOU ARE NO MATCH FOR THE CUBE.')
    green_swordsman = lab_12_combatants.Enemy('A warrior renowned for his... green-ness. ',
                                              'The Green Warrior', 120, 'Straight punch', 12, 'Green Headbutt', 18,
                                              'A shame. They could not match up to my GREEN.')
    dragon = lab_12_combatants.Enemy('The guardian of the village. Something is controlling the dragon\'s behavior.', 'The Dragon',
                                     250, 'Flame Breath', 12, 'Wrathful Claw', 25, 'You were mighty... But not mighty enough.')
    fiend = lab_12_combatants.Enemy('The being terrorizing the village.\nIt has been empowered by defeated heroes.',
                                    'Underworld Fiend', 300, 'Wrath', 17, 'Siphon', 7, 'And with this... None will be able to rival me again!')
    # encounter flags
    dialogue_flag = False
    fiend_dialogue = False
    dragon_dialogue = False
    cube_defeated = False
    long_defeated = False
    dragon_defeated = False
    fiend_defeated = False
    battle = False
    done = False

    flag = False
    player_class = None
    current_enemy = None
    while not flag:
        print(warrior.class_name, ':', warrior.player_description)
        print(rogue.class_name, ':', rogue.player_description)
        print(wizard.class_name, ':', wizard.player_description)
        class_select = input('What is your class of choice? ').lower()
        if 'wizard' in class_select:
            player_class = wizard
            flag = True
        elif 'rogue' in class_select:
            player_class = rogue
            flag = True
        elif 'warrior' in class_select:
            player_class = warrior
            flag = True
        else:
            print('Please select a valid class.')

    print("\nYou have awoken from what feels like years of sleep. You are currently in a mansion."
          "\nIt would be wise to seek out someone who knows why.\nInput C for controls.")

    item_list = lab_12_items.populate_items()
    while not done:
        # One time dialogue
        if lab_12_rooms.current_room == 8 and not dialogue_flag:
            print('\n Guard: \"You must be the new hero. I\'m the town\'s chief guard. I\'ll fill you in on what\'s going on.\n'
                  'To the southeast, through the forest, is a fortress. A dragon inhabits it. That dragon\n'
                  'used to protect us, but now it antagonizes the village...\n'
                  'I don\'t know what caused it to change, but as of now,\n'
                  'it believes that only the strong have a right to live.\n'
                  'Those who cannot protect themselves must die. That is the dragon\'s doctrine.\n'
                  'Countless heroes like yourself have tried to stop the dragon, but they never return...\n'
                  'If you wish to follow in their footsteps, take care in preparing yourself.\"')
            dialogue_flag = True

        # Post Dragon fight dialogue
        if lab_12_rooms.current_room == 15 and dragon_defeated and not dragon_dialogue:
            print('\n As you defeated the dragon, the ring on its claw fell off. The dragon crushes the ring underfoot.'
                  '\n Dragon:\"Thank you, hero. That ring was controlling me. It was the work of the village mayor.'
                   '\n He has been leading heroes to fight me, to be killed as tribute for a demon.'
                  '\n You must return to the village, and stop the demon.\"')
            dragon_dialogue = True
        if lab_12_rooms.current_room == 8 and not fiend_dialogue and dragon_defeated:
            print('\nFollowing the advice of the dragon, you confront the mayor.')
            print('\n', player_class.class_name, ': \"Why are you sacrificing the heroes who come to help your village?\"')
            print('\n', 'Mayor: \"The demon threatened our village. It asked for strong sacrifices, so the heroes were lead to fight the dragon. '
                  'It was to protect the people who live here!\"')
            if player_class == warrior:
                print('\n', player_class.class_name, ': \"Cowardly and foolish. Lead me to the fiend and I will destroy it. I will enact the will of the sacrificed heroes.')
            elif player_class == rogue:
                print('\n', player_class.class_name, ': \"Fool. Show me the way. I will protect the village properly.')
            else:
                print('\n', player_class.class_name, ': \"You were deceived. You aren\'t sacrificing heroes to protect the people, it\'s just making '
                                            'that demon stronger. \nYou\'ve forsaken both the lives of those who fight to protect you, '
                                            'and the people of the village. Now, show me the way, so I can correct your mistakes.')
            print('\nMayor: \"It inhabits the graveyard to the north. Good luck...')
            fiend_dialogue = True

        if fiend_defeated:
            print('\n You have defeated the underworld fiend. Peace has returned to the village.'
                  '\n The mayor was imprisoned for his crimes, and replaced by the guard captain.'
                  '\n The dragon became the guardian of the village once more.'
                  '\n As for the', player_class.class_name, ', it is the duty of heroes to protect those in need.'
                  '\n The job does not end. Go forth, and live up to your name.')
            done = True
            break
        # Battle 1 - Cube
        elif lab_12_rooms.current_room == 11 and not cube_defeated:
            current_enemy = cube
            battle = True
            exploration_player.pause()
            cube_fight_player = cube_fight.play(0.5, 0, True)
            lab_12_models.cube_draw()
        # Battle 2 - Green warrior
        elif lab_12_rooms.current_room == 13 and not long_defeated:
            current_enemy = green_swordsman
            battle = True
            exploration_player.pause()
            long_fight_player = long_fight.play(0.5, 0, True)
            lab_12_models.green_draw()
        # Battle 3 - Dragon
        elif lab_12_rooms.current_room == 15 and not dragon_defeated:
            current_enemy = dragon
            battle = True
            exploration_player.pause()
            dragon_fight_player = dragon_fight.play(0.5, 0, True)
            lab_12_models.dragon_draw()
        # Final Battle - Fiend
        elif lab_12_rooms.current_room == 16 and dragon_defeated and not fiend_defeated:
            current_enemy = fiend
            battle = True
            exploration_player.pause()
            fiend_fight_player = fiend_fight.play(0.5, 0, True)
            lab_12_models.fiend_draw()

        if not battle:
            print('\n', lab_12_rooms.room_list[lab_12_rooms.current_room].description)

            for item in item_list:
                if item.room_number == lab_12_rooms.current_room:
                    print(item.i_description)
            command_words = input("What is your command? (n, e, s, w, d, u, i, get, use, drop, status) ").lower().split(" ")

            if command_words[0] == 'n':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].north

            elif command_words[0] == 's':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].south

            elif command_words[0] == 'e':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].east

            elif command_words[0] == 'w':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].west

            elif command_words[0] == 'd':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].down

            elif command_words[0] == 'u':
                lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].up

            elif command_words[0] == 'c':
                print('N, E, S, W, for cardinal directions, '
                      'D, U, for down and up,\nI for inventory, '
                      'get to retrieve items, drop to drop items, and use to use items.'
                      'status for character status.\nQ to quit.')

            elif 'get' in command_words:
                found = False
                for item in item_list:
                    if item.room_number == lab_12_rooms.current_room:
                        item.room_number = INV
                        print('\nYou retrieved the ', item.i_name, '.')
                        found = True
                if not found:
                    print('No items are present.')

            elif 'status' in command_words:
                print('You have', player_class.class_hp, 'health and', player_class.mana, 'mana.'
                      ' Your attack stat is', player_class.class_attack, '.')

            elif command_words[0] == 'i':
                found = False
                for item in item_list:
                    if item.room_number == INV:
                        print('Your inventory contains', item.i_name)
                        found = True
                if not found:
                    print('Your inventory is empty.')

            elif 'drop' in command_words:
                drop = input("What would you like to drop? ").lower()

                for i in range(len(item_list)):
                    if item_list[i].room_number == INV:
                        if drop == item_list[i].i_name:
                            item_list[i].room_number = lab_12_rooms.current_room

            elif 'use' in command_words:
                use = input("What would you like to use? ").lower()
                for i in range(len(item_list)):
                    if item_list[i].room_number != INV:
                        if use == item_list[i].i_name:
                            print('\nYou do not have that item.')
                    elif item_list[i].room_number == INV:
                        if use == item_list[i].i_name:
                            if use == 'mirror':
                                print('\nYou look dashing.')

                            elif use == 'key':
                                if lab_12_rooms.current_room == 12:
                                    print('\nThe chest was opened, but the key broke in the process.')
                                    key = get_item(item_list, 'key')
                                    key.room_number = OOP
                                    charm = get_item(item_list, 'charm')
                                    charm.room_number = 12
                                else:
                                    print('\nThat isn\'t the right place to use this.')

                            elif use == 'charm':
                                print('\nThe charm is absorbed into your weapon. You\'ve gotten stronger.')
                                player_class.class_attack += 3
                                charm = get_item(item_list, 'charm')
                                charm.room_number = OOP

                            elif use == 'elixir':
                                print('\nYou\'ve been fully healed.')
                                player_class.class_hp = player_class.class_max_hp
                                elixir = get_item(item_list, 'elixir')
                                elixir.room_number = OOP

                            elif use == 'talisman':
                                player_class.class_max_hp += 5
                                player_class.class_hp = player_class.class_max_hp
                                print('\nYou\'ve been fully healed, and your max HP increased. Max HP is now', player_class.class_max_hp, '.')
                                talisman = get_item(item_list, 'talisman')
                                talisman.room_number = OOP

                            elif use == 'blessing':
                                player_class.class_max_hp += 5
                                player_class.class_attack += 2
                                player_class.max_mana += 5
                                print('\nThe dragon\'s blessing empowers you. All stats have increased.')
                                blessing = get_item(item_list, 'blessing')
                                blessing.room_number = OOP

            elif command_words[0] == 'q':
                print("Game over.")
                done = True

            else:
                print("Please give a valid command.")
                continue

            # check for valid choice
            if lab_12_rooms.next_room == None:
                print("You can't go that way!")
                continue

            # if all is well, set new room
            lab_12_rooms.current_room = lab_12_rooms.next_room

            # ///////////////////////////////////////////////////// Battle /////////////////////////////////////////////////////
        elif battle:
            while current_enemy.monster_hp > 0 and player_class.class_hp > 0:
                guard = 1
                distance = 4
                action = False
                print('You are challenged by', current_enemy.monster_name, '!')
                print('Combat commands: B: Basic attack, 1: Skill 1, 2: Skill 2, advance, retreat, wait, status')
                print('Input \"controls\" to show commands, and \"skills\" for class skill info.')
                while current_enemy.monster_hp > 0:
                    if player_class.class_hp <= 0:
                        print(current_enemy.m_taunt, '\n You were defeated. Game over.')
                        battle = False
                        cube_defeated = True
                        long_defeated = True
                        dragon_defeated = True
                        done = True
                        break

                    print(current_enemy.monster_name, 'is ', distance, 'meters away.')
                    while not action:
                        command_words = input("What is your command? ").lower().split(" ")
                        # Basic attack
                        if command_words[0] == 'b' and player_class.p_range >= distance:
                            damage = player_class.class_attack
                            current_enemy.monster_hp -= damage
                            if current_enemy.monster_hp < 0:
                                current_enemy.monster_hp = 0
                            print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                                  ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                  current_enemy.monster_hp, 'HP remaining.')
                            # Mana regeneration on basic attack
                            if player_class.mana < player_class.max_mana:
                                if player_class == wizard:
                                    player_class.mana += 10
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                elif player_class == warrior:
                                    player_class.mana += 5
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                else:
                                    player_class.mana += 7
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                            action = True

                        elif command_words[0] == 'b' and player_class.p_range < distance:
                            print('A valiant attempt. You are too far away.')
                            action = True

                        # Movement commands
                        elif 'wait' in command_words:
                            if player_class == wizard:
                                player_class.mana += 20
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            else:
                                player_class.mana += 10
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            print('You remain in place, recovering mana.', player_class.mana, 'mana remains.',
                                  ' Your HP is', player_class.class_hp, '.')
                            action = True

                        elif 'advance' in command_words:
                            if distance == 1:
                                print('You\'re at point blank range.')
                            else:
                                distance -= 1
                                if player_class == rogue:
                                    player_class.mana += 7
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                else:
                                    player_class.mana += 4
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                print('You advanced one meter. Mana recovered.', player_class.mana, 'mana remains.',
                                      ' Your HP is', player_class.class_hp, '.')
                                action = True
                        elif 'status' in command_words:
                            print('You have', player_class.class_hp, 'HP,', player_class.class_attack, 'attack, and', player_class.mana, 'Mana. '
                                    'The enemy has', current_enemy.monster_hp, 'HP. You are', distance, 'meters from the enemy. '
                                    'Your enemy is', current_enemy.monster_name, '.\n', current_enemy.monster_description)
                        elif 'controls' in command_words:
                            print('Combat commands: B: Basic attack, 1: Skill 1, 2: Skill 2, advance, retreat, wait')
                        elif 'skills' in command_words:
                            print('Skill 1:', player_class.p_skill1, ':', player_class.p_skill1desc,
                                  '\nSkill 2:', player_class.p_skill2, ':', player_class.p_skill2desc,
                                  '\nPassive:', player_class.passive)

                        elif 'retreat' in command_words:
                            retreat_roll = random.randrange(0, 7)
                            if retreat_roll <= 2:
                                r_storage = 2
                                distance += r_storage
                            elif retreat_roll > 2 and retreat_roll <= 5:
                                r_storage = 3
                                distance += r_storage
                            else:
                                r_storage = 4
                                distance += r_storage
                            if player_class == rogue:
                                player_class.mana += 7
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            else:
                                player_class.mana += 4
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            print('You retreated', r_storage, 'meters. Mana recovered.', player_class.mana, 'mana remains.',
                                  ' Your HP is', player_class.class_hp, '.')
                            action = True
                        # Skill 1
                        elif command_words[0] == '1':
                            # Wizard skill 1
                            if player_class == wizard and player_class.mana >= 40:
                                player_class.class_attack *= 3
                                if player_class.class_attack < 30:
                                    print('Your mana amplifies your power. That\'s more like it.')
                                elif player_class.class_attack > 30 and player_class.class_attack < 100:
                                    print('Your strength is overflowing.')
                                elif player_class.class_attack > 100:
                                    print('This is excessive.')
                                player_class.mana -= 40
                                print(player_class.mana, 'mana remains.')
                                action = True
                            elif player_class == wizard and player_class.mana < 40:
                                print('You don\'t have enough mana.')

                                # Warrior skill 1
                            elif player_class == warrior:
                                if distance <= 3 and player_class.mana >= 15:
                                    print('You swing your sword destructively. The strike invigorates you.')
                                    damage = player_class.class_attack * (warrior.class_max_hp // warrior.class_hp)
                                    current_enemy.monster_hp -= damage
                                    warrior.class_hp = warrior.class_hp + ((warrior.class_max_hp - warrior.class_hp) // 3)
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    action = True
                                elif distance > 3 and player_class.mana >= 15:
                                    print('You swing your sword destructively... From too far away.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 15:
                                    print('You don\'t have enough mana.')

                                    # Rogue skill 1
                            else:
                                if distance < 4 and player_class.mana >= 15:
                                    print('They won\'t be prepared for this.')
                                    damage = player_class.class_attack * 4
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    guard = 2
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    distance = 1
                                    action = True
                                elif distance >= 4 and player_class.mana >= 15:
                                    print('They won\'t be prepared for this... But neither were you. You missed.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    distance = 2
                                    action = True
                                elif player_class.mana < 15:
                                    print('You don\'t have enough mana.')
                        # Skill 2
                        # Wizard skill 2
                        elif command_words[0] == '2':
                            if player_class == wizard and player_class.mana >= 20:
                                if distance <= 4:
                                    print('Turn them to ash.')
                                    damage = player_class.class_attack * 3
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 20
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif distance > 4:
                                    print('Turn them to ash. Or try to, like you just did. You missed.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 20
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 20:
                                    print('You don\'t have enough mana.')
                            # Warrior skill 2
                            elif player_class == warrior:
                                if player_class.mana >= 10:
                                    print('Your defenses are raised. You gain 10 mana.')
                                    guard = 3
                                    player_class.mana += 10
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 10:
                                    print('You don\'t have enough mana.')
                                    print(player_class.mana, 'mana remains.')
                            # Rogue skill 2
                            elif player_class == rogue:
                                if distance <= 3 and player_class.mana >= 25:
                                    print('They won\'t be catching you anytime soon.')
                                    distance += 2
                                    damage = player_class.class_attack * 2
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 25
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif distance > 3 and player_class.mana >= 25:
                                    print('They won\'t be catching you anytime soon. '
                                          'But you won\'t be catching them either with aim like that.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    distance += 2
                                    player_class.mana -= 25
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 25:
                                    print('You don\'t have enough mana.')
                                    print(player_class.mana, 'mana remains.')
                        else:
                            print('Please input a valid command.')
                    # Victory, ending battle
                    if current_enemy.monster_hp <= 0:
                        print('You have defeated', current_enemy.monster_name, '!')
                        # Wizard gains extra HP and mana on win
                        if player_class == wizard:
                            wizard.class_max_hp += 5
                            wizard.class_hp += 5
                            wizard.max_mana += 10
                            wizard.mana = wizard.max_mana
                            charm = get_item(item_list, 'charm')
                            blessing = get_item(item_list, 'blessing')
                            wizard.class_attack = 5
                            if charm.room_number == OOP:
                                wizard.class_attack += 3
                            if blessing.room_number == OOP:
                                wizard.class_attack += 2
                            # Warrior regains 66% of missing HP on victory and gains more max HP, gains slight attack boost as well
                        elif player_class == warrior:
                            warrior.mana = warrior.max_mana
                            warrior.class_max_hp += 10
                            warrior.class_hp = warrior.class_hp + ((warrior.class_max_hp - warrior.class_hp) // 1.5)
                            warrior.class_attack += 1
                        else:
                            # Rogue gets more attack and max mana on victory
                            rogue.max_mana += 15
                            rogue.mana = rogue.max_mana
                            rogue.class_attack += 3
                        if current_enemy == cube:
                            cube_defeated = True
                            arcade.stop_sound(cube_fight_player)
                            exploration_player.play()
                        elif current_enemy == green_swordsman:
                            long_defeated = True
                            arcade.stop_sound(long_fight_player)
                            exploration_player.play()
                        elif current_enemy == dragon:
                            dragon_defeated = True
                            arcade.stop_sound(dragon_fight_player)
                            exploration_player.play()
                        elif current_enemy == fiend:
                            fiend_defeated = True
                            arcade.stop_sound(fiend_fight_player)
                            print('\n', player_class.class_name, ': \"May those who were sacrificed rest in peace.')
                        battle = False
                    else:
                        # Enemy Movement
                        if distance > 1:
                            if distance >= 3:
                                enemy_move = random.randrange(0, 2)
                                if enemy_move == 1:
                                    distance -= 2
                                    print(current_enemy.monster_name, 'moved 2 meters.')
                                    action = False
                                    if distance <= 0:
                                        distance = 1
                                else:
                                    print(current_enemy.monster_name, 'moved 1 meter.')
                                    action = False
                                    distance -= 1
                                    if distance <= 0:
                                        distance = 1
                            elif distance > 1:
                                distance -= 1
                                print(current_enemy.monster_name, 'moved 1 meter.')
                                action = False
                        if distance == 1:
                            enemy_action = random.randrange(0, 4)
                            if enemy_action == 1:
                                print(current_enemy.monster_name, 'makes no action.')
                                action = False

                            enemy_attack = random.randrange(0, 2)
                            if enemy_attack == 1 and enemy_action != 1:
                                print(current_enemy.monster_name, 'is using', current_enemy.m_skill1)
                                enemy_damage = current_enemy.m_skill1_dmg
                                dmg_received = enemy_damage // guard
                                player_class.class_hp -= dmg_received
                                print('You received', dmg_received, 'damage.')
                                guard = 1
                                if current_enemy == dragon:
                                    print('The dragon\'s fire siphons your mana.')
                                    player_class.mana -= 5
                                    if player_class.mana < 0:
                                        player_class.mana = 0
                                action = False
                            else:
                                if enemy_action != 1:
                                    print(current_enemy.monster_name, 'is using', current_enemy.m_skill2)
                                    enemy_damage = current_enemy.m_skill2_dmg
                                    dmg_received = enemy_damage // guard
                                    player_class.class_hp -= dmg_received
                                    print('You received', dmg_received, 'damage.')
                                    guard = 1
                                    if current_enemy == dragon:
                                        print('The dragon\'s claws sunder your defenses.')
                                        guard = 0.5
                                    elif current_enemy == fiend:
                                        print('The fiend\'s magic steals your life.')
                                        current_enemy.monster_hp += 3
                                    action = False
main()
