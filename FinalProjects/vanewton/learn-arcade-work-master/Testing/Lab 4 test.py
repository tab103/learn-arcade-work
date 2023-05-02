import arcade
def main():
    print()
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
    print()
    print("A. Drink from canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")


user_choice = input("What is your choice? ")
if user_choice.upper() == "Q":
    print ("Get outta here!")
    break

elif user_choice.upper() == "E":
    print("You have traveled " + str(miles_traveled) + " miles.")
    print("You have " + str(canteen) + " drinks left.")
    print("The natives are " + str(miles_traveled - natives_distance) + " miles away.")





main()