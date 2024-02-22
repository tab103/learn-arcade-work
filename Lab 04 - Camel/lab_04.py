import random


def menu():
    print("""
    A. Eat some beef jerky
    B. Run at a normal speed
    C. Run at full speed
    D. Break for the night
    E. Status Check
    F. Name your horse
    Q. Quit
    """)


def main():

    print("Welcome to the Great Plains")
    print("You have stolen a horse from one of the many tribes that inhabit the Great Plains.")
    print("Attempt to escape back to the American settlement across the Great Plains region before you're caught")

    miles_traveled = 0
    hunger = 0
    horse_tiredness = 0
    tribe_distance = -20
    beef_jerky = 5
    daily_travel = 0

    done = False

    while not done:
        menu()
        user_choice = input("What are you going to do? ").upper()
        if user_choice == 'Q':
            done = True

        elif user_choice == 'E':
            print("Miles Traveled:", miles_traveled)
            print("Amount of jerky left:", beef_jerky)
            print("Number of miles the natives are behind you:", miles_traveled - tribe_distance)

        elif user_choice == 'A':  # eat
            if beef_jerky == 0:
                print("You are out of food!!!")
            elif beef_jerky > 0:
                hunger = 0
                beef_jerky -= 1

        elif user_choice == 'B':  # moderate speed
            daily_travel += random.randrange(7, 14)
            miles_traveled += daily_travel
            print("Miles traveled:", daily_travel)
            horse_tiredness += 1
            hunger += 1
            if random.randrange(21) == 0:
                print("You meet a generous man who restocks your jerky supply")
                beef_jerky = 5
            tribe_distance += random.randrange(7, 12)

        elif user_choice == 'C':  # Full speed
            daily_travel += random.randrange(10, 22)
            miles_traveled += daily_travel
            print("Miles traveled:", daily_travel)
            hunger += 1
            horse_tiredness += random.randrange(1, 4)
            tribe_distance += random.randrange(7, 14)
            if random.randrange(21) == 0:
                print("You meet a generous man who restocks your jerky supply")
                beef_jerky = 5

        elif user_choice == 'D':  # Rest
            horse_tiredness = 0
            print("Your horse is rested and happy")
            tribe_distance += random.randrange(4, 9)

        elif user_choice == 'F':
            input("What will you name your horse?")
            print("The horse simply looks at you in a confused manner and continues as before.")
        if hunger > 4:
            print("You're starved")

        if horse_tiredness > 4 and horse_tiredness < 8:
            print("Your horse is tired")

        if horse_tiredness >= 8:
            print("Your horse died")
            print("The tribe will catch you before long")
            done = True

        elif tribe_distance + 15 >= miles_traveled:
            print("The tribe is catching up!")

        if tribe_distance >= miles_traveled:
            print("The tribe has caught you and exacted revenge")
            print("Game Over")
            done = True

        if miles_traveled >= 200:
            print("You have won and escaped from the natives!!!")
            done = True
        if miles_traveled <= 200:
            daily_travel = 0


main()
