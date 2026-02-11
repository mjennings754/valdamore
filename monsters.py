import random
from player import Player
class Monster:
    def __init__(self, health, attack_damage, combat_level):
        self.health = health
        self.attack_damage = attack_damage
        self.combat_level = combat_level

    def __str__(self):
        return "You enter the Taverby Dungeon...\nRRRAAAARGGGHHHH!"
    
    def attack(self, player):
        if self.health <= 0:
            print("The lesser demon has been defeated")
            return
        
        self.health -= 4
        print(f"The Lesser Demon has {self.health} health remaining")

        player.add_experience("Attack", 50)

        if self.health <= 0:
            print(f"The Lesser Demon has been killed by {player.username}")

    
lesser_demon = Monster(1000, 4, 87)
