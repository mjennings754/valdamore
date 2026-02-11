from player import Player
print("Welcome to Valdamore!")

username = input("Enter a display name: ")

player = Player(username)

print(f"{player.username} begins their journey in Cambridge")