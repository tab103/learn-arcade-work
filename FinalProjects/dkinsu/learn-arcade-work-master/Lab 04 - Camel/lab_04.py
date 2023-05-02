import random


def main():
    drinks = 3
    thirst = 0
    tired = 0
    traveled = 0
    natdistance = -20

    # Instructions
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # While loop for main actions
    done = False
    while not done:
        # Starting with game ending conditions
        # Native game over
        if (traveled < 200) and (natdistance >= traveled):
            print("The natives have caught you!")
            print("Game over.")
            done = True

        # Tiredness game over
        elif (tired > 8):
            print("Your camel is dead.")
            print("Game over.")
            done = True

        # Thirst game over
        elif (thirst > 6):
            print("You died of thirst!")
            print("Game over.")
            done = True

        # Win
        elif (traveled >= 200):
            print("You made it across the desert! You won!")
            done = True
        else:
            print("A. Drink from your canteen.")
            print("B. Ahead moderate speed.")
            print("C. Ahead full speed.")
            print("D. Stop for the night.")
            print("E. Status check.")
            print("Q. Quit.")
            prompt = input("What is your choice? ")

            # Drinking from canteen to reduce thirst, printing error if canteen is empty
            if prompt.upper() == "A":
                if drinks > 0:
                    drinks -= 1
                    thirst = 0
                else:
                    print("Your canteen is empty.")

            # Moving moderate speed, random roll for oasis after move
            elif (prompt.upper() == "B"):
                natmove = random.randrange(7, 15)
                modmove = random.randrange(5, 13)
                tired += 1
                thirst += 1
                traveled = modmove + traveled
                print("You traveled ", modmove, " miles.")
                natdistance = natmove + natdistance
                if random.randrange(20) == 0:
                    print("You found an oasis!")
                    tired = 0
                    thirst = 0
                    drinks = 3

            # Moving full speed, random roll for oasis after move
            elif (prompt.upper() == "C"):
                natmove = random.randrange(7, 15)
                fullmove = random.randrange(10, 21)
                randtired = random.randrange(1, 4)
                tired = tired + randtired
                thirst += 1
                traveled = fullmove + traveled
                print("You traveled ", fullmove, " miles.")
                natdistance = natmove + natdistance
                if random.randrange(20) == 0:
                    print("You found an oasis!")
                    tired = 0
                    thirst = 0
                    drinks = 3

            # Resting, moving natives and resetting tiredness
            elif (prompt.upper() == "D"):
                natmove = random.randrange(7, 15)
                tired = 0
                print("The camel is happy.")
                natdistance = natmove + natdistance

            # Status Check
            elif (prompt.upper() == "E"):
                nattraveled = traveled - natdistance
                print("You have traveled ", traveled, " miles.")
                print("Your canteen has ", drinks, " drinks remaining.")
                print("The natives are ", nattraveled, " miles behind you.")

            # Quitting Game
            elif (prompt.upper() == "Q"):
                print("Game Over")
                done = True

            # Extra conditional statements pertaining to thirst, tiredness, and native distance
            if ((thirst > 4) and (thirst != 7)):
                print("You are thirsty.")

            if ((tired > 5) and (tired != 9)):
                print("Your camel is getting tired.")

            if ((natdistance < traveled) and (natdistance > 0)):
                if ((traveled - natdistance) < 15):
                    print("The natives are getting close!")
            elif ((natdistance <= 0) and (traveled - natdistance) < 15):
                print("The natives are getting close!")


main()
