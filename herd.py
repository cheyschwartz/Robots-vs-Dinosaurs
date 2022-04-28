
from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one = Dinosaur('TRex', 50)
        dinosaur_two = Dinosaur('Stegosaurus', 50)
        dinosaur_three = Dinosaur('Raptor', 50)

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)


