import random
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives!")
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen = 3
    done = False
    while not done:
        print("A. Drink from canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        if user_choice == "Q":
            print("Get outta here!")
            done = True
        elif user_choice == "E":
            print("You have traveled",miles_traveled,"miles.")
            print("You have",canteen,"drinks left.")
            print("The natives are",(miles_traveled - natives_distance),"miles away.")
            done = False
        elif user_choice == "D":
            print("You have decided to rest for the night.")
            print("Your camel is resting and happy! :)")
            print("The natives are",miles_traveled - natives_distance,"miles away.")
            natives_distance = natives_distance + random.randrange(7, 12)
            camel_tiredness = 0
        elif user_choice == "C":
            print("You have chosen to continue at full speed.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            natives_distance = natives_distance + random.randrange(7, 14)
            miles_traveled = miles_traveled + random.randrange(10,20)
            oasis = random.randrange(0,20)
            if oasis == 4:
                print("You have found an oasis!")
                canteen = 3
                camel_tiredness = 0
                thirst = 0
        elif user_choice == "B":
            print("You go ahead at moderate speed.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            miles_traveled = miles_traveled + random.randrange(10, 20)
            natives_distance = natives_distance + random.randrange(7, 14)
            oasis = random.randrange(0, 20)
            if oasis == 7:
                print("You have found an oasis!")
                canteen = 3
                camel_tiredness = 0
                thirst = 0
        elif user_choice == "A":
            print("You chose to drink from your canteen.")
            canteen = canteen - 1
            thirst = 0
        if thirst >= 6:
            print("You are thirsty.")
        if thirst >= 8:
            print("You have died of thirst!")
            done = True
        if camel_tiredness >= 8:
            print("Your camel is dead!")
            done = True
        if camel_tiredness > 5 and camel_tiredness < 8:
            print("Your camel is getting tired...")
        if natives_distance >= miles_traveled:
            print("The natives caught you.")
            done = True
        elif miles_traveled - natives_distance <= 15:
            print("The natives are getting close!")
        if miles_traveled >= 200:
            print("You have escaped!")
            done = True



main()








