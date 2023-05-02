class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

# not in class!
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Room 0- King's room
    room = Room("You are in the king's quarters. There is a door to the south."
                , None, 2, None, None)
    room_list.append(room)

    # Room 1- Princess room
    room = Room("You are in the Princess's room. There is a door to the east.", None, None, 2, None)
    room_list.append(room)


    # Room 2- North hallway
    room = Room("You are in the north hallway, you may go north, south, east, or west.", 0, 4, 1, 3)
    room_list.append(room)

    # Room 3- The Commons
    room = Room("You are in the commons, there is a door to the west.", None, None, None, 2)
    room_list.append(room)


    # Room 4- South hallway
    room = Room("You are in the south hallway. There is a door to the west and south.", 2, 6, None, 5)
    room_list.append(room)

    # Room 5- Knight's room
    room = Room("You have entered the knight's room. There is a door to the west and south.", None, None, None, 4)
    room_list.append(room)

    # Room 6- Throne room
    room = Room("You have entered the throne room.", 4, None, None, None)
    room_list.append(room)

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south
        # add other directions

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'q':
            print("You have quit the game!")
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
