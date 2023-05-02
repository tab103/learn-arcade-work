import random


# main loop
def main():
    """Game instructions"""
    print("Welcome to Camel! \nYou have stolen a camel to make your way across the great Mobi desert. \nThe natives want their camel back and are chasing you down! Survive your desert trek and outrun the natives.")
    """variables and their default values"""
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_from_natives = -30
    drinks_in_canteen = 3
    while not done:
        print("\nA. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. \nE. Status check \nQ. Quit.")
        # ask for user choice
        user_choice = input("\nWhat would you like to do? ")
        if user_choice.upper() == 'Q':
            print(f"You quit. \nMiles traveled: {miles_traveled} \nDrinks in canteen: {drinks_in_canteen} \nThe natives are {-distance_from_natives} miles behind you.")
            done = True

        elif user_choice.upper() == "A" and drinks_in_canteen > 0:
            thirst = 0
            drinks_in_canteen -=1
        elif user_choice.upper() == 'B':
            if random.randrange(20) == 0:
                drinks_in_canteen = 3
                print("YOU FOUND AN OASIS!")
            random_numbera = random.randint(5, 12)
            miles_traveled += random_numbera
            thirst += 1
            camel_tiredness += random.randint(1,3)
            distance_from_natives += (random.randint(7,14)-random_numbera)
            print(f"You have traveled {miles_traveled} miles.")
        elif user_choice.upper() == 'C':
            # chance of finding an oasis
            if random.randrange(20) == 0:
                drinks_in_canteen = 3
                print("YOU FOUND AN OASIS!")
            random_numberb = random.randint(10, 20)
            miles_traveled += random_numberb
            thirst += 1
            camel_tiredness += random.randint(1,3)
            distance_from_natives += (random.randint(7,14)-random_numberb)
            print(f"You have traveled {miles_traveled} miles.")
        elif user_choice.upper() == 'D':
            distance_from_natives += random.randint(7,14)
            camel_tiredness = 0
            if distance_from_natives <0:
                print("Camel is happy.")
        elif user_choice.upper() == 'E' and not distance_from_natives >= 0:
            print(f'You have traveled {miles_traveled} miles. \nThe natives are {distance_from_natives} miles behind you. \nYou have {drinks_in_canteen} drinks in your canteen left. \nYour thirst level is {thirst}. \nYour tiredness level is {camel_tiredness}')

        # died of thirst
        if thirst > 6:
            print(f"GAME OVER! \nYou died of thirst. \nNext time monitor your thirst level.")
            done = True

        if camel_tiredness > 8:
            print("GAME OVER! Your camel died of tiredness.")
            break

        if 6 < camel_tiredness < 9:
            print("Your camel is getting tired.")


        # thirst reminder
        if 4 < thirst < 7 and not miles_traveled >=0:
            print("CAUTION!! You are thirsty.")

        # when canteen is empty
        if drinks_in_canteen == 0:
            print("CAUTION!! Your canteen is empty.")

        # natives are close signal
        if -15 <= distance_from_natives < 0:
            print("The natives are getting close.")

        # natives have caught up
        if distance_from_natives >= 0 and not user_choice == "Q":
            print("GAME OVER!! The natives have captured you.")
            done = True

        # to check game success
        if miles_traveled >=200:
            print ("CONGRATULATIONS!! You have crossed the desert.")
            done = True


# call the main function
main()