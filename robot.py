from weapon import Weapon


class Robot:
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Tomahawk', 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{dinosaur.name} is down to {dinosaur.health}!")
        print('')
