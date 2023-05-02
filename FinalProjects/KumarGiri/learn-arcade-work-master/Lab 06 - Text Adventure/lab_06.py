# the class to create different rooms
class Room:
    def __init__(self, description, east, west, north, south):
        self.description = description
        self.east = east
        self.west = west
        self.north = north
        self.south = south

# not in class!
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Bedroom one - 0 - (description, east, west, north, south)
    room0 = Room("You are in the bedroom one, there is a door to the east.", 1, None, None, None)
    room_list.append(room0)

    # South Hall -1- (description, east, west, north, south)
    room1 = Room("You are in the south hall, there are doors to your east, west, and north.", 2, 0, 4, None)
    room_list.append(room1)

    # Store Room -2-
    room2 = Room("You are in the store room, there is a door to your west", None, 1, None, None)
    room_list.append(room2)

    # Kitchen -3-
    room3 = Room("You are in the kitchen, there are doors to your east and west", 9, 4, None, None)
    room_list.append(room3)

    # Living Room -4-
    room4 = Room("You are in the living room, there are doors in all four directions", 3, 5, 7, 1)
    room_list.append(room4)

    # Bedroom two -5-
    room5 = Room ("You are in bedroom two, there are doors to your east and west", 4, None, None, None)
    room_list.append(room5)

    # Bathroom -6-
    room6 = Room("You are in the bathroom, there is a door to your east", 1, None, None, None)
    room_list.append(room6)

    # North Hall -7-
    room7 = Room("You are in the north hall, there are doors in all four directions", 8, 6, 9, 4)
    room_list.append(room7)

    # Bedroom three -8-
    room8 = Room("You are in bedroom three, there is a door to your west", None, 7, None, None)
    room_list.append(room8)

    # Balcony -9-
    room9 =Room("You have arrived on the balcony, enjoy the view. To go back inside, there is a door in your south.", None, None, None, 7)
    room_list.append(room9)

    while not done:
        print("")
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (e, w, n, s)").lower()

        # To exit the game
        if direction[0] == 'q':
            print('You have exited the game.')
            break
        # Checking directions to enter different rooms
        if direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south

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