import random


# defined the function
def stat(mt, ct, nby, fs, ms, dic, cth, ust):
    # return result to caller, which is stat down below
    result = MILES_TRAVELED, CAMEL_TIREDNESS, NATIVES_BEHIND_YOU, FULL_SPEED, MODERATE_SPEED, DRINKS_IN_CANTEEN, CAMEL_THIRST, USER_THIRST
    return result


# stats that are used
MILES_TRAVELED = 0
CAMEL_TIREDNESS = 0
NATIVES_BEHIND_YOU = -20
FULL_SPEED = random.randrange(10, 21)
MODERATE_SPEED = random.randrange(5, 13)
FULL_SPEED_NATIVES = random.randrange(7, 15)
MODERATE_SPEED_NATIVES = random.randrange(7, 15)
DRINKS_IN_CANTEEN = 3
CAMEL_THIRST = 0
USER_THIRST = 0

# hold the stats in a variable
result = stat(MILES_TRAVELED, CAMEL_TIREDNESS, NATIVES_BEHIND_YOU, FULL_SPEED, MODERATE_SPEED, DRINKS_IN_CANTEEN,
              CAMEL_THIRST, USER_THIRST)


# initial prompt to user
def intro_sentences():
    # initial print statement to user
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.\n")


intro_sentences()

# the game is not finished
Done = False
# while game is not finished
while not Done:

    def main():
        # choices for user to pick from
        print("A. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed. ")
        print("D. Stop for the night. ")
        print("E. Status check. ")
        print("Q. Quit.")

    # user is asked question and gives a response
    USER_INPUT = input("What is your choice?")
    if USER_INPUT.upper() == "E":
        print("\nMiles traveled:", MILES_TRAVELED)
        print("Drinks in canteen:", DRINKS_IN_CANTEEN)
        # miles that natives are behind user
        print("The natives are", MILES_TRAVELED - NATIVES_BEHIND_YOU, "miles behind you.\n")

    # user picks q = quit
    elif USER_INPUT.upper() == "Q":
        print("\nGame will end now!")
        # End game
        Done = True
        exit()

    # user picks a = drink from canteen
    elif USER_INPUT.upper() == "A":
        USER_INPUT = input("Do you take a drink?")
        if USER_INPUT.upper() == "YES" or USER_INPUT.upper() == "Y" and DRINKS_IN_CANTEEN > 0 and USER_THIRST > 0:
            DRINKS_IN_CANTEEN = DRINKS_IN_CANTEEN - 1
            USER_THIRST = 0
            print("You have", DRINKS_IN_CANTEEN, "drinks left in canteen.")
        # if user thirst less than 0, print you are not thirsty
        if USER_THIRST <= 0:
            print("You are not thirsty.")
        # if user has no water in canteen, no more water left to drink
        if DRINKS_IN_CANTEEN == 0:
            USER_THIRST = USER_THIRST
            print("No more water is in your canteen.")

    # user picks b = moderate speed
    elif USER_INPUT.upper() == "B":
        MILES_TRAVELED = MILES_TRAVELED + MODERATE_SPEED
        print("\nYou travel", MILES_TRAVELED, "miles.")
        NATIVES_BEHIND_YOU = NATIVES_BEHIND_YOU + MODERATE_SPEED_NATIVES
        print("The native are now", NATIVES_BEHIND_YOU, "miles behind you from your current position.")
        CAMEL_TIREDNESS = CAMEL_TIREDNESS + 1
        print("Your camel's tiredness raised to", CAMEL_TIREDNESS)
        USER_THIRST = USER_THIRST + 1
        print("Your thirst is", USER_THIRST, "\n")

    # user picks c = full speed
    elif USER_INPUT.upper() == "C":
        MILES_TRAVELED = MILES_TRAVELED + FULL_SPEED
        print("\nYou travel", MILES_TRAVELED, "miles.")
        NATIVES_BEHIND_YOU = NATIVES_BEHIND_YOU + FULL_SPEED_NATIVES
        print("The native are now", NATIVES_BEHIND_YOU, "miles behind you from your current position.")
        CAMEL_TIREDNESS = CAMEL_TIREDNESS + 1
        print("Camel's tiredness is", CAMEL_TIREDNESS)
        USER_THIRST = USER_THIRST + 1
        print("Your thirst is", USER_THIRST, "\n")

    # user picks d = rest for night
    elif USER_INPUT.upper() == "D":
        CAMEL_TIREDNESS = 0
        print("\nYour camel is happy :).")
        NATIVES_BEHIND_YOU = NATIVES_BEHIND_YOU + random.randrange(7, 15)
        print("The native are now", NATIVES_BEHIND_YOU, "miles behind you from your current position.\n")

    # natives are close
    if 0 < NATIVES_BEHIND_YOU < 15 and not USER_INPUT.upper() == "E" or not USER_INPUT.upper() == "A":
        print("The natives are close!")
    # you are thirsty
    if USER_THIRST == 4 or USER_THIRST == 5 and not Done and not USER_INPUT.upper() == "E":
        print("You are thirsty!")

    # you die of thirst
    if USER_THIRST > 6 and not Done:
        print("You died of thirst!")
        Done = True
        exit()

    # camel is tired
    if CAMEL_TIREDNESS > 5 and not Done and not USER_INPUT.upper() == "E":
        print("Your camel is getting tired.")

    # camel dies of exhaustion
    if CAMEL_TIREDNESS > 8 and not Done:
        print("Your camel is died of exhaustion!")
        Done = True
        exit()

    # natives caught you
    if NATIVES_BEHIND_YOU == 0 and not Done:
        print("The natives have caught up!")
        Done = True
        exit()

    # camel is thirsty
    if CAMEL_THIRST == 4 or CAMEL_THIRST == 5 and not Done and not USER_INPUT.upper() == "E":
        print("Your camel is getting thirsty!")

    # camel dies of thirst
    if CAMEL_THIRST > 8 and not Done:
        print("Your camel died of thirst!")
        Done = True
        exit()

    # you beat the game
    if MILES_TRAVELED >= 200:
        print("\nYou made it across the desert. You win!")
        exit()

    # 1 / 20 of finding an oasis
    if random.randrange(1, 21) == 1:
        print("\nYou found an oasis!")
        if CAMEL_TIREDNESS > 0:
            CAMEL_TIREDNESS = 0
            print("Your camel is no longer tired.")
        elif CAMEL_TIREDNESS == 0:
            print("Your camel's tiredness is already at zero.")
        if USER_THIRST > 0:
            USER_THIRST = 0
            print("You are no longer thirsty.")
        elif USER_THIRST == 0:
            print("You drank water, and it did nothing.")
        if DRINKS_IN_CANTEEN == 3:
            print("Your canteen is already at max.\n")
        elif DRINKS_IN_CANTEEN == 0 or DRINKS_IN_CANTEEN == 1 or DRINKS_IN_CANTEEN == 2:
            print("You refill your canteen.\n")
            DRINKS_IN_CANTEEN = 3
        else:
            print("You found nothing.\n")

main()
