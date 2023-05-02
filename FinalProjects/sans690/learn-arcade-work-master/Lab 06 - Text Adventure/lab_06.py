class Room:

    # constructor
    def __init__(self, description, north, east, south, west):
        # attributes
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


# creating instances of rooms in the class
def main():
    # the current room is bedroom 1, which is 0
    current_room = 0
    # defining what rooms there are/ where they have doors if any and adding them to the list
    room_list = []
    room_0 = Room("You are in the living room.\nThere is a door to the east.", None, 1, None, None)
    room_list.append(room_0)
    room_1 = Room("You are in the south hallway.\nThere is a door to the west and east and an opening to the north.",
                  4, 2, None, 0)
    room_list.append(room_1)
    room_2 = Room("You are in the dining room.\nThere is a door to the west.", None, None, None, 1)
    room_list.append(room_2)
    room_3 = Room("You are in the master bedroom.\nThere is a door to the east.", None, 4, None, None)
    room_list.append(room_3)
    room_4 = Room("You are in the north hallway.\nThere is a door to the west and east and an opening to the south.",
                  6, 5, 1, 3)
    room_list.append(room_4)
    room_5 = Room("You are in the kitchen.\nThere is a door to the west.", None, None, None, 4)
    room_list.append(room_5)
    room_6 = Room("You are in the balcony.\nThere is a door to the south.", None, None, 4, None)
    room_list.append(room_6)
    Done = False

    while Done is False:
        # while the program is not finish do this code
        print(room_list[current_room].description)
        # prompts the user a question to which they respond with a direction
        direction = input("Which way would you like to go? (n s e w)\n").lower()
        if direction[0] == "n":
            # the next room is equal to the parameter north in current room
            next_room = room_list[current_room].north
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move north.")
                continue
            # if there is a room to move to in that direction, you can move that direction
            elif next_room == room_list[current_room].north:
                print("You moved to the north.")
                # if able to move, the room you move to is now your current room
                current_room = next_room

        # if user doesn't pick north, then user can pick to move east with input
        elif direction[0] == "e":
            # the next room is equal to the parameter east in current room
            next_room = room_list[current_room].east
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move east.")
                continue
            elif next_room == room_list[current_room].east:
                print("You moved to the east.")
                # if able to move, the room you move to is now your current room
                current_room = next_room

        # if user doesn't pick north or east, then user can pick to move south with input
        elif direction[0] == "s":
            # the next room is equal to the parameter south in current room
            next_room = room_list[current_room].south
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move south.")
                continue
            elif next_room == room_list[current_room].south:
                print("You moved to the south.")
                # if able to move, the room you move to is now your current room
                current_room = next_room

        # if user doesn't pick north, east, or south, then user can pick to move west with input
        elif direction[0] == "w":
            # the next room is equal to the parameter west in current room
            next_room = room_list[current_room].west
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move west.")
                continue
            elif next_room == room_list[current_room].west:
                print("You moved to the west.")
                # if able to move, the room you move to is now your current room
                current_room = next_room

        # if user doesn't pick north, east, south, or west, then user can pick to quit the game
        elif direction[0] == "q":
            print("Quiting game.")
            exit()
        # any other input is invalid
        else:
            print("Invalid input!")


main()
