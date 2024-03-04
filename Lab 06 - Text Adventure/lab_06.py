class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    current_room = 0
    next_room = 0
    insanity = 0
    done = False
    # lobby starting spot (0)
    room = Room("You stand in a dark, dreary foyer. You note all the windows are boarded up. "
                "There are doors to your east, south, and west."
                " The door to your south is locked. There is a staircase to your north", 6, 5, None, 1)
    room_list.append(room)

    # Dining Room (1)
    room = Room("You are in what seems to be a dining room, the table you note is covered in rotten"
                " food and flies. You can go North or East.", 2, 0, None, None)
    room_list.append(room)

    # Kitchen (2)
    room = Room("You are now in the kitchen which smells of rotten food and has rotten food scattered everywhere."
                "You can go East or South", None, 3, 1, None)
    room_list.append(room)

    # Servant's Quarters (3)
    room = Room("As you enter what seems to be the servant's quarters the lights fade and you here a loud thump from"
                "above you. You can go East or West.", None, 4, None, 2)
    room_list.append(room)

    # Laundry Room (4)
    room = Room("You now stand in the laundry room which seems to be an irregularity throughout the house. The lights"
                "in this room are on and everything is organized with clothes seemingly just cleaned and ready to be"
                "put away. You can go South or West.", None, None, 5, 3)
    room_list.append(room)

    # Sitting Room (5)
    room = Room("You enter what seems to be a sitting room, it is as dark and unkept as the lobby with cobwebs covering"
                "most of the furniture, you note that there is one chair that is absent of all cobwebs. You can go"
                "North or West.", 4, None, None, 0)
    room_list.append(room)

    # Stairs Center (6)
    room = Room("You hear each step creak underneath you as you ascend the staircase. At the top you can go to the East"
                ", back down the stairs to the south, or West", None, 12, 0, 7)
    room_list.append(room)

    # Upper Left Hall (7)
    room = Room("As you enter a long hallway and you realize you can't see the end of it. You also see a"
                "door to the west. You can head further south to the other end of the hallway, through the door or back"
                "to the staircase.", None, 6, 8, 10)
    room_list.append(room)

    # Lower Left Hall (8)
    room = Room("As you progress further down the hall you notice another door to the west. The pitch black continues"
                "until you nearly walk into a wall marking the end of the hall. As you turn around you note"
                "there is a wall where you came from, leaving only one direction to travel in: West.", None,
                None, None, 9)
    room_list.append(room)

    # Library (9)
    room = Room("As you enter the door shuts behind you. The room seems to be a library but for some reason all the"
                "books are on the floor, but one book remains on the northern bookshelf. You have two options, go North"
                "and move the book or go East through the door", 10, 8, None, None)
    room_list.append(room)

    # Bedroom 1 (10)
    room = Room("You are now in what seems to be an old bedroom. You notice a small journal on the bed that has the"
                "same phrase written in it over and over\"HE'S COMING FOLLOW THE BLOOD\". You see three doors, "
                "a heavy one to the south"
                "and normal doors to the north and east", 11, 7, 9, None)
    room_list.append(room)

    # Bathroom 1 (11)
    room = Room("You now seem to be in the bathroom and on the mirror written in old, dried blood the word"
                " \"REDRUM\". You can only go south back into the bedroom.", None, None, 10, None)
    room_list.append(room)

    # Upper Right Hall (12)
    room = Room("As you enter the hallway, you see a trail of blood on the wall and floor going south down the hall. "
                "You also see a door to the north and another to the east.", 13, 14, 15, 6)
    room_list.append(room)

    # Bathroom 2 (13)
    room = Room("As you enter the bathroom you notice a victorian style doll sitting by the mirror pointing at the door"
                " you entered from. It's eyes follow you as you move. On the mirror written in blood is a message"
                "\"HURRY HE ONLY WAITS SO LONG\". You can only go back through the door to the South.", None, None,
                12, None)
    room_list.append(room)

    # Bedroom 2 (14)
    room = Room("As you enter you hear a little girl calling to you from the room to the South saying to come to her."
                "Otherwise the room seems to have belonged to a young man but on the ceiling you see marks that seem to"
                " have broken fingernails and blood, as if someone was dragged across it. You can only go in the door"
                "you came from to the West", None, None, None, 12)
    room_list.append(room)

    # Lower Right Hall (15)
    room = Room("The trail of blood leads to a door as you hear the voice of a little girl telling you to come inside"
                "and urging you to hurry before the monster gets you too. You can go East to the little girl's voice"
                "or you can go North back up the Hallway.", 12, 16, None, None)
    room_list.append(room)

    # Bedroom 3 (16)
    room = Room("As you enter you notice a translucent little girl standing by an open window. She calls to you and "
                "says \"If you want to escape you must jump out the window.\" This room seems to be in good condition"
                "and there is nothing horrifying in it which is irregular noting what you have seen elsewhere."
                "You can go East and jump out the window,"
                "or you can go West back into the hallway", None, 17, None, 15)
    # Outside (17)
    room_list.append(room)
    room = Room("As you land you hear scratching coming from within the walls of the house as it sounds like something"
                " is trying to get out. As you flee the house you hear a bloodcurdling roar come from the house, but "
                "nothing follows you further.", None, None, None, None)
    room_list.append(room)

    if current_room == 17:
        print("You Escaped")
        done = True
    if insanity > 25:
        print("You scream as a monstrous creature tears it way out of the wall and attacks you. It's eyeless head"
              "roars in triumph as it tears you to pieces with it's long jagged claws and drags you into the wall with"
              "it.")
        print("You didn't escape in time")
        done = True

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n e s w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north
            insanity += 1

        elif direction[0] == 'e':
            next_room = room_list[current_room].east
            insanity += 1

        elif direction[0] == 's':
            next_room = room_list[current_room].south
            insanity += 1

        elif direction[0] == 'w':
            next_room = room_list[current_room].west
            insanity += 1

        else:
            print("Please pick a valid direction")
            continue

        if next_room == None:
            print("You can't go that way")
            continue
        current_room = next_room
    if insanity > 6 and insanity < 10:
        print("You hear whispers from the walls but can't make out what they are saying.")
    if insanity > 10 and insanity < 18:
        print("You hear the voices louder but they scream now in panic followed by growling.")
    if insanity > 18 and insanity < 25:
        print("You hear fervent scratching from the walls as the voices scream louder and louder.")


main()
