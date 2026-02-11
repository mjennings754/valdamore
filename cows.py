from player import Player
import random
class Cow:
    def __init__(self, health, attack_damage, combat_level):
        self.health = health
        self.attack_damage = attack_damage
        self.combat_level = combat_level

    def __str__(self):
        return "There's a cow nearby."
    
    def attack(self, player):
        if self.health <= 0:
            print("The cow is already dead")
            return
        
        self.health -= 3
        print(f"Cow has {self.health} health remaining")

        player.add_experience("Attack", 50)

        if self.health <= 0:
            print("The cow has been killed!")
            self.health = 8
            print("A new cow appears")

            loot_table = ["Raw beef", "Cowhide"]
            drop = random.choice(loot_table)
            player.add_item(drop)

cow1 = Cow(8, 2, 2)