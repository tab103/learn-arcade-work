
#import
import random

def main ():
    print("Welcome to Camel! "
          "You have stolen a camel to make your way across the great Mobi desert."
          "The natives want their camel back and are chasing you down!"
          "Survive your desert trek and outrun the natives.")


    miles_traveled = 0
    thirst = 40
    camel_energy = 100
    natives_distance = 20
    done = False


    # constants
    CANTEEN_LEVEL = 3
    DISTANCE_TO_TRAVEL = 200


    def status():
        print("miles_traveled: " + str(miles_traveled))
        print("camels energy: " + str(camel_energy))
        print("drinks of water left: " + str(CANTEEN_LEVEL))
        print("Time until you need to drink... " + str(thirst))
        print("The hungry natives are only " + str(natives_distance) + (" miles behind you!"))


#main game while loops
    while done is False:
        print("A. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed! ")
        print("D. Stop for the night. ")
        print("E. Status check. ")
        print("Q. Quit.")


        answer = input("What is your answer: ")


        if answer.upper() == "Q":
            done = True
            print("You got to scared of the natives. They over took you and ate you or something.")
            natives_distance -= random.randrange(3)
            thirst = 30


        elif answer.upper() == "A":
            done = False
            CANTEEN_LEVEL -= 1
            print("You have taken a drink of water.")
            if CANTEEN_LEVEL == 0:
                print("You,  no longer have any water")
            natives_distance -= 1



        elif answer.upper() == "B":
            miles_traveled += random.randrange(5, 12)
            camel_energy -= random.randrange(5, 10)
            thirst -= random.randrange(10)
            for i in range(20):
                if random.randrange(30) == 0:
                    print("You have found an oasis!")
                    CANTEEN_LEVEL == 3
                    camel_energy == 100
                    thirst == 40

        elif answer.upper() == "C":
            miles_traveled += random.randrange(7, 14)
            camel_energy -= random.randrange(8, 15)
            thirst -= random.randrange(10)
            for i in range(20):
                if random.randrange(30) == 0:
                    print("You have found an oasis!")
                    CANTEEN_LEVEL == 3
                    camel_energy == 100
                    thirst == 40

        elif answer.upper() == "D":
            camel_energy = 100
            natives_distance -= random.randrange(20)
            thirst -= random.randrange(5)


        elif answer.upper() == "E":
            status()







        if thirst <= 20:
            CANTEEN_LEVEL -= 1
            print("you are thirsty. You should take a drink.")
            if CANTEEN_LEVEL == 0:
                print("You,  no longer have any water")
            natives_distance -= random.randrange(7)
            thirst = 30
        if thirst <= 0:
                print("you died of thirst")
                break
        if camel_energy <= 0:
            answer.upper() == "D"
            camel_energy = 100
            natives_distance -= random.randrange(3, 7)
            print("You camel is tired and must take a rest! You can continue in the morning.")
            status()

        if miles_traveled >= DISTANCE_TO_TRAVEL:
            print("You have escaped the desert and the natives!!")
            break

        if natives_distance <= 0:
            print("You got eaten by the natives, and they took the camel.")
            break


main()
