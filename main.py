from time import sleep

from player import Player
from cows import *
print("Welcome to Valdamore!")

username = input("Enter a display name: ")

player = Player(username)

print(f"{player.username} begins their journey in Cambridge")
sleep(1)
while True:
    print("\nWhat would you like to do?")
    print("1) Adventure around")
    print("2) Go to cow area")
    print("3) Check stats")
    print("4) Quit")

    userinput = int(input("> "))

    if userinput == 1:
        print("You go adventure around Valdamore!")
    elif userinput == 2:
        print("You see a cow")
        userinput = int(input("1) Attack the cow 2) Leave the cow alone \n"))
        if userinput == 1:
            cow1.attack(player)
        else:
            print("The cow continues to eat grass")

    elif userinput == 3:
        print(f"Attack: {player.skills['Attack']}")
        print(f"Attack XP: {player.experience['Attack']}")

    elif userinput == 4:
        print("Goodbye!")
        break

    else:
        print("invalid option")