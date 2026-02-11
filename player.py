MAX_SKILL_LEVEL = 99

class Player:
    def __init__(self, username):
        self.username = username
        self.skills = {
            "Attack": 1,
        }
        self.experience = {
            skill: 0 for skill in self.skills
        }

    def add_experience(self, skill, amount):
        self.experience[skill] += amount
        print(f"Gained {amount} xp in {skill}")

        self.check_level_up(skill)

    
    def check_level_up(self, skill):
        current_level = self.skills[skill]
        current_xp = self.experience[skill]

        xp_needed = current_level * 120

        while current_xp > xp_needed and current_level < MAX_SKILL_LEVEL:
            self.skills[skill] += 1
            current_level += 1
            print(f"Your {skill} level is now {current_level}.")

            xp_needed = current_level * 120

