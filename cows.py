class Cow:
    def __init__(self, health, attack_damage, combat_level):
        self.health = health
        self.attack_damage = attack_damage
        self.combat_level = combat_level

    def __str__(self):
        return "There's a cow nearby."

cow1 = Cow(8, 2, 2)