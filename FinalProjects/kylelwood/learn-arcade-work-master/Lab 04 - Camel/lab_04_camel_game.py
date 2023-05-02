import random

def main():

    """introduces player to the game"""
    print("\nWelcome to Camel Game")
    print("You have stolen a camel from a tribe of natives and must get back to town.")
    print("You will have to travel 200 miles to get to safety.")
    print("Do what you must to keep the natives at a distance.\n")

    done = False
    miles_traveled = 0
    camel_thirst = 0
    natives_traveled = -20
    canteens_remaining = 6
    distance_to_town = 200
    moderate_speed = random.randrange(4, 9)
    fast_speed = random.randrange(10, 16)
    print()

    # Main loop of game
    while not done:
        print("A: Continue quickly")
        print("B: Continue at moderate pace")
        print("C: Check health status")
        print("D: Drink from canteen")
        print("Q: Quit")
        print()
        player_input = input("What is your choice? ")
        if player_input.lower() == "q":
            done = True

    # Move ahead quickly
        elif player_input.lower() == "a":
            print("\nYou are moving ahead very quickly")
            miles_traveled = miles_traveled + fast_speed
            camel_thirst = camel_thirst + 3
            natives_traveled += random.randrange(4, 9)
            natives_behind = miles_traveled - natives_traveled
            distance_to_town -= random.randrange(10, 16)
            print("You have gained", natives_behind, "miles away from the natives!")


    # Move ahead moderately
        elif player_input.lower() == "b":
            print("\nYou are moving ahead at a normal speed.")
            print("The natives are a little farther back.")
            natives_behind = miles_traveled - natives_traveled
            miles_traveled = miles_traveled + moderate_speed
            camel_thirst = camel_thirst + 1
            distance_to_town -= random.randrange(4, 9)


    # Check health status
        elif player_input.lower() == "c":
            print("\nYour thirst level is", camel_thirst, "out of 10!")
            print("The natives are", natives_behind, "miles away.")
            print("You have", distance_to_town, "miles until you reach town safely.")
            print("You have", canteens_remaining, "bottles of water remaining.")

    # Drink some water
        elif player_input.lower() == "d":
            if camel_thirst >= 8:
                camel_thirst += 2
            elif camel_thirst == 9:
                camel_thirst += 1
            if canteens_remaining <= 0:
                print("You have no more refills!")
            print("\nYou have gained", camel_thirst, "health points!")
            print("You have lost", natives_behind, "miles to the natives.")

    # in-game checks
            if natives_behind <= 10:
                print("The natives are very close!")
            if miles_traveled <= natives_behind:
                print("""You have been caught!
            The camel has been returned to the natives!
            You are now their prisoner.""")
                done = True
            if camel_thirst <= 5:
                print("Thirst is halfway drained.")
            if camel_thirst <= 2:
                print("Your camel is dying of thirst!")
            if camel_thirst <= 0:
                print("""You lose!
            The camel has died!
            You will be caught soon.""")
                done = True
            if miles_traveled >= 200:
                print("You arrived in town safely!")
                print("The natives stopped chasing you!")
                print("You win!")
                done = True

main()