from time import sleep

from player import Player
from cows import *
print("Welcome to Valdamore!")

username = input("Enter a display name: ")

player = Player(username)

print(f"{player.username} begins their journey in Cambridge")
sleep(1)
print(cow1)
userinput = int(input("1) Attack the cow 2) Leave the cow alone \n"))
if userinput == 1:
    print("You attack the cow")
    cow1.attack(player)
else:
    print("You let the cow chew on some grass!")