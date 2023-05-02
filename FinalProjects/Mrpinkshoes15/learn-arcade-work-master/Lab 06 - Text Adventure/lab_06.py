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
    done = False

# entry_way - room 1 (description, north, east, south, west)
    room = Room("Welcome to your DOOM... You are in the entry way, there is a hallway to the east.", None, 1, None, None)
    room_list.append(room)

# hallway - room 2
    room = Room("You are in the hallway, you can continue east.", 6, 2, None, None)
    room_list.append(room)

# main room - room 3
    room = Room("you are in the main room now, you may continue to the east or to the north.", None, 1, None, 1)
    room_list.append(room)

# bed_room 1 - room 4
    room = Room("you are in the first bed room continue north.", 1, None, None, None)
    room_list.append(room)

# bed_room 2 - room 5
    room = Room("You are in the second bedroom now, you may continue north or back to the south.", 1, None, 1, None)
    room_list.append(room)

# bed_room 3 - room 6
    room = Room("You are in the third bed room and final bedroom. you may jump through the east or west windows.", None, 1, None, 1)
    room_list.append(room)

# westside wilderness
    room = Room("You have escaped run free while you still can!", None, 1, None, None)
    room_list.append(room)

# eastside wilderness
    room = Room("You have escaped run free while you still can!", None, None, None, 1)
    room_list.append(room)


    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w) ").lower()
        if direction[0] == "n":
            next_room = room_list[current_room].north

        elif direction[0] == "s":
            next_room = room_list[current_room].south

        elif direction[0] == "e":
            next_room = room_list[current_room].east

        elif direction[0] == "w":
            next_room = room_list[current_room].west

        else:
            print("Please pick valid direction.")
            continue

        if next_room == None:
            print("you can't walk through walls, sorry.")
            continue


        current_room = next_room

main()