class Room:
    """This is a class"""
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    """This is the main function"""
    # Creating empty list
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # bedroom 2 - 0 ( description, north, east, south, west) 0
    room = Room("\nyou are in the second room, there is a door to the east.", None, 1, None, None)
    room_list.append(room)

    # south hall
    room = Room("\nyou are in the south hall, there is a door to the north and east.", 4, 2, None, 0)
    room_list.append(room)

    # Dinning room
    room = Room("\nyou are in the Dining room, there is a door to the north and west.", 5, None, None, 1)
    room_list.append(room)

    # bedroom 1
    room = Room("\nyou are in the first bedroom, there is a door to the east.", None, 4, None, None)
    room_list.append(room)

    # North hall
    room = Room("\nyou are in the North hall, there is a door to the North, East, South, And West", 6, 5, 1, 3)
    room_list.append(room)

    # Kitchen
    room = Room("\nyou are in the Kitchen, there is a door to the south and west.", None, None, 2, 4)
    room_list.append(room)

    # Balcony
    room = Room("\nyou are in the balcony, there is a door to the south", None, None, 4, None)
    room_list.append(room)

    # add rest of rooms
    while not done:
        print(room_list[current_room].description)
        direction = input("which way would you like to go? (n s e w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 's':
            next_room = room_list[current_room].south

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'q':
            print("Thank you for playing")
            done = True

            # add other directions
        else:
            print("please pick a valid direction")
            continue

            # check for valid choice
        if next_room is None:
            print("you cant go that way!")
        else:
            # if all is well, set new room
            current_room = next_room


main()
