class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# not in class!


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Bedroom 2 - 0 - (description, north, east, south, west)
    room = Room("You are in the second bedroom, there is a door to the east.", None, 1, None, None)
    room_list.append(room)

    # South Hall - 1
    southhall = Room("You are in the south hall.\nThere are doors to the north, east, and west.", 4, 2, None, 0)
    room_list.append(southhall)

    # Dining Room - 2
    diningroom = Room("You are in the dining room.\nThere are doors to the west and north.", 5, None, None, 1)
    room_list.append(diningroom)

    # Bedroom 1 - 3
    bedroom1 = Room("You are in the first bedroom.\nThere is a door to the east.", None, 4, None, None)
    room_list.append(bedroom1)

    # North Hall - 4
    northhall = Room("You are in the north hall.\nThere are doors to the north, east, south, and west.", 6, 5, 1, 3)
    room_list.append(northhall)

    # Kitchen - 5
    kitchen = Room("You are in the kitchen.\nThere are doors to the south and west.", None, None, 2, 4)
    room_list.append(kitchen)

    # Balcony - 6
    balcony = Room("You are on the balcony.\nThere is a door to the south.", None, None, 4, None)
    room_list.append(balcony)

    print("Welcome to the haunted mansion!\nDo your best to escape!\nInput q to quit.")

    while not done:
        # rudimentary gameplay through avoidance of enemies
        # dining room ghost
        if room_list[current_room] == diningroom:
            print("There is a hungry looking ghost present.\nYou can fight, or avoid it.\n(f, or n, e, s, w input)")
            fight = input("Fight? ").lower()
            if fight[0] == 'f':
                print("Why did you think you could beat a ghost? Game over.")
                break

        # kitchen vampire
        if room_list[current_room] == kitchen:
            print("There is a vampire standing in the kitchen.\nQuick, throw the nearby garlic at him!\n(yes/no)")
            throw = input("Throw garlic? ").lower()
            if throw[0] == 'y':
                print("The vampire is dazed. Best to leave now. ")
            else:
                print("You probably should have thrown that garlic. Now you're the vampire's meal. Game Over.")
                break

        # bedroom 1 werewolf
        if room_list[current_room] == bedroom1:
            print("There is a werewolf in the bedroom! It's too fast to avoid! Game over.")
            break

        # balcony escape
        if room_list[current_room] == balcony:
            print("Maybe you can jump off the balcony to escape.")
            jump = input("Jump? (yes/no) ").lower()
            if jump[0] == 'y':
                print("You safely land from the balcony, and escape the creatures of the night.\nYou win! Game over.")
                break

        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w) ").lower()

        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'q':
            print("Game over.")
            break

        else:
            print("Please pick a valid direction.")
            continue

        # check for valid choice
        if next_room == None:
            print("You can't go that way!")
            continue

        # if all is well, set new room
        current_room = next_room


main()
