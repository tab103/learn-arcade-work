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

    # add rest of the rooms

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north

        # add other directions

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