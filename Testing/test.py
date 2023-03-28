import random

class Room:
    number_of_rooms = 0
    def __init__(self, description, north, south, east, west, multi_path = False): # called by Room(description, north south, east, west)
        self.description = description # initialize the instance variables description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.has_monster = (random.randrange(1, 11) == 5)   # 10% chance of having a monster in the room

        Room.number_of_rooms += 1 # increment number of rooms

        def add_food(self, val):
            pass

class Kitchen(Room):
    def __init__self(self, description, north, south, east, west):
        super().__init__(description, north, south, east, west)
        self.has_food = (random.randrange(1, 3) == 2)   # 50% chance there is food in the kitchen

    def add_food(self, val):
        self.has_food = val


class Bedroom(Room):
    def __init__self(self, description, north, south, east, west):
        super().__init__(description, north, south, east, west)
        self.has_hidden_door = (random.randrange(1, 6) == 2)   # 50% chance there is food in the kitch

class Hall(Room):
    def __init__self(self, description, north, south, east, west, multi_path):
        super().__init__(description, north, south, east, west, multi_path)

class Dining(Room):
    def __init__self(self, description, north, south, east, west):
        super().__init__(description, north, south, east, west)
        self.people_eating = (random.randrange(1, 3) == 2)  # 50% chance people are eating


def main():
    rooms = []
    # desc, north, south, east, west
    rooms.append(Bedroom("Bedroom 4", None, None, None, 4)) #0
    rooms.append(Bedroom("Bedroom 3", None, None, None, 4)) #1
    rooms.append(Bedroom("Bedroom 2", None, 1, None, 4)) #2
    rooms.append(Hall("Hall", None, None, 99, 99, True)) #3
    rooms.append(Bedroom("Bedroom 1", None, None, 4, None)) #4
    rooms.append(Dining("Dining Room", 7, None, 4, None)) #5
    rooms.append(Kitchen("Large Kitchen", None, 6, 4, None)) #6

    while True:
        for room in rooms:
            print(room.description)

        rm = int(input(f"There are {Room.number_of_rooms} which do you want to see? "))
        print(rooms[rm])

main()



