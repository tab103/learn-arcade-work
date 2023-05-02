import random


def main():
    native_traveled = -20
    camel_tiredness = 0
    miles_traveled = 0
    thirst = 1
    canteen = 3
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")


    done = False
    while not done:
        natives_behind = miles_traveled - native_traveled
        full_speed = random.randrange(10, 21)
        moderate_speed = random.randrange(5, 13)
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("what is your choice? ")
        if user_choice.upper() == 'Q':
            print("thanks for playing")
            done = True
        # status check
        elif user_choice.upper() == "E":
            print("Miles traveled", miles_traveled)
            print("Drinks in canteen", canteen)
            print("your camel has", camel_tiredness, "amount of fatigue")
            print("The natives are", natives_behind, "miles behind you")
        # stop for the night
        elif user_choice.upper() == "D":
            camel_tiredness *= 0
            print("camel is happy")
            native_traveled += random.randrange(7, 15)
        # moving full speed ahead
        elif user_choice.upper() == "C":
            print("you traveled ", full_speed, "miles")
            miles_traveled += full_speed
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            native_traveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)
        # moving in moderate speed
        elif user_choice.upper() == "B":
            print("you traveled ", moderate_speed, "miles")
            miles_traveled += moderate_speed
            thirst += 1
            camel_tiredness += 1
            native_traveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)
        # drinking canteen
        elif user_choice.upper() == "A":
            if canteen == 0:
                print("you are out of water")
            else:
                canteen -= 1
                thirst *= 0
                print("you have ", canteen, "drinks left and you are no longer thirsty")
        oasis = random.randrange(20);
        if oasis == 0:
            camel_tiredness *= 0
            thirst *= 0
            canteen = 3
            print("you found an oasis! After taking a drink you filled your canteen")
        if natives_behind <= 15:
            print("the natives are drawing near!")
        if native_traveled >= miles_traveled:
            print("the natives caught and beheaded you")
            print("you are dead!")
            done = True
        if thirst > 4 and thirst <= 6 and not done:
            print("you are thirsty")
        if thirst > 6:
            print("you are thirsty")
            done = True
        if camel_tiredness > 5 and camel_tiredness <= 8 and not done:
            print("your camel is getting tired.")
        if camel_tiredness > 8:
            print("your camel is dead")
            done = True


main()
