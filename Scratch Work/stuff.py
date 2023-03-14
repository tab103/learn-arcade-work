class Room:
    """This class defines the rooms"""

    def __init__(self, description, north, south, east, west):
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

    # Living Room - 0 - (description, north, south, east, west)
    room = Room("""
You are in the living room.
There is a hallway to the North, kitchen to the East and porch to the South.""", 2, 6, 1, None)
    room_list.append(room)

    # Kitchen - 1 - (description, north, south, east, west)
    room = Room("""
You are now in the kitchen. There is hot food on the table.
You can only go back into the living room from the kitchen.""", None, None, None, 0)
    room_list.append(room)

    # Main Hallway - 2 - (description, north, south, east, west)
    room = Room("""
You are in the main hallway of the house.
There is a bathroom to the North, master bedroom to the West, and spare bedroom to the East.
You can re-enter the living room if you wish.""", 3, 0, 5, 4)
    room_list.append(room)

    # Bathroom - 3 - (description, north, south, east, west)
    room = Room("""
You are now in the bathroom.
Nothing in here but a shower, toilet and sink.
You must go back to the main hallway to continue.""", None, 2, None, None)
    room_list.append(room)

    # Master Bedroom - 4 - (description, north, south, east, west)
    room = Room("""
You are in the master bedroom.
You see a bed and a few pieces of furniture. Nothing fancy.
You must go back to the main hallway to continue.""", None, None, 2, None)
    room_list.append(room)

    # Spare Bedroom - 5 - (description, north, south, east, west)
    room = Room("""
You are now in the spare bedroom.
You can see a bed and a table, but that's it.
You must go back to the main hallway to continue.""", None, None, None, 2)
    room_list.append(room)

    # Porch - 6 - (description, north, south, east, west)
    room = Room("""
You have reached the side porch.
It is a really nice night out tonight.
You see a few chairs and a table.
You must re-enter the living room to continue.""", 0, None, None, None)
    room_list.append(room)

    while not done:
        print(room_list[current_room].description)
        direction = input("""
Which way would you like to go? (N, S, E, W, Q to quit) """).lower()

        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'q':
            done = True

        else:
            print("Please pick a valid direction.")
            continue

        # check for valid choice
        if next_room == None:
            print("There is no doorway here.")
            continue

        # if all is well, set new rooms
        current_room = next_room


main()