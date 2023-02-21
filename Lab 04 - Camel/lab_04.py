"""
Lab 4: Camel Game
"""
import random


CAMEL_DEAD = 8
CAMEL_TIRED = 5
MAX_THIRST = 6
THIRSTY = 4
MILES_TO_TRAVEL = 200
NATIVE_WARNING_DISTANCE = 15
CANTEEN_CAPACITY = 3

def menu():
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop and rest.
    E. Status check.
    Q. Quit. 
    """)
    choice = input("Your choice?")
    return choice[0].upper()


def intro():
    print("""
    Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and outrun the natives.
    """)


def print_status(traveled, canteen, natives):
    print('You have traveled ', traveled, ' miles.')
    print('You have ',canteen,' drinks left in you canteen.')
    print('The natives are ', traveled - natives, ' behind you.')


def main():
    intro()
    done = False # game loop sentinel
    miles_traveled = 0
    thirst = 0.0
    camel_tiredness = 0
    natives_distance = -30 # how far back
    drinks_in_canteen = 3
    while not done:
        choice = menu()
        if choice == 'Q':   # quit?
            print("Thank you for playing!")
            break
        elif choice == 'E': # status
            print_status(miles_traveled, drinks_in_canteen, natives_distance)
        elif choice == 'D':  # stop and rest
            camel_tiredness = 0
            print("The camel is happy!")
            natives_distance += random.randrange(7, 15) # move closer a random amount
        elif choice == 'C':  # full speed ahead
            miles_traveled += random.randrange(10, 21)
            print('You have traveled ', miles_traveled, ' miles.')
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_distance += random.randrange(7, 15)
        elif choice == 'A':  # drink from canteen
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                thirst = 0
            else:
                print('Sorry, your canteen is empty!')
        elif choice == 'B': # moderate speed
            miles_traveled += random.randrange(5, 13)
            print('You have traveled ', miles_traveled, ' miles.')
            thirst += 1
            camel_tiredness += 1
            natives_distance += random.randrange(7, 15)

        # check conditions
        # check thirst condition
        if thirst > MAX_THIRST:
            print('You died of thirst!')
            break
        elif thirst > THIRSTY:
            print('You are thirsty.')

        # check tiredness
        if camel_tiredness > CAMEL_DEAD:
            print("Your camel is dead!, game over")
            break
        elif camel_tiredness > CAMEL_TIRED:
            print("Your camel is getting tired")

        # check natives
        if natives_distance >= miles_traveled:
            print('The natives have caught you, game over!')
            break
        elif miles_traveled - natives_distance < NATIVE_WARNING_DISTANCE:
            print('The natives are getting close!')

        # check total distance
        if miles_traveled > MILES_TO_TRAVEL:
            print('You have escaped the natives, survived the desert, and won the game!')
            break

        # check for oasis
        if choice == 'B' or choice == 'C': # must be traveling to find an oasis
            if random.randrange(1,20) == 5:    # just pick a number in the range
                print('You found an oasis!')
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = CANTEEN_CAPACITY

# start game
main()