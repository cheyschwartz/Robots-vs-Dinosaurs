from fleet import Fleet
from herd import Herd
import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
    
    def display_welcome(self):
        print('Welcome to the Robots vs Dinosaurs Game!')

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            rando_roll = random.randint(1, 10)
            if rando_roll % 2 == 0:
                self.dino_turn()
                if len(self.fleet.robots) > 0:
                    self.robo_turn()
            else:
                self.robo_turn()
                if len(self.herd.dinosaurs) > 0:
                    self.dino_turn()

    def dino_turn(self):
        self.show_dino_opponent_options()
        dino_choice = int(input('Which dinosaur is going to attack?'))
        print('')
        self.show_robot_opponent_options()
        robot_choice = int(input('Which robot is going to defend?'))
        print('')
        self.herd.dinosaurs[dino_choice].attack(
            self.fleet.robots[robot_choice])
        if self.fleet.robots[robot_choice].health <= 0:
            print(f'Oh no! {self.fleet.robots[robot_choice].name} has died!')
            self.fleet.robots.remove(self.fleet.robots[robot_choice])


    def robo_turn(self):
        self.show_robot_opponent_options()
        robot_choice = int(input('Which robot is going to attack?'))
        print('')
        self.show_dino_opponent_options()
        dino_choice = int(input('Which dinosaur is going to defend?'))
        print('')
        self.fleet.robots[robot_choice].attack(
            self.herd.dinosaurs[dino_choice])
        if self.herd.dinosaurs[dino_choice].health <= 0:
            print(f'Oh no! {self.herd.dinosaurs[dino_choice].name} has died!')
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_choice])


    def show_dino_opponent_options(self):
        print('Select your robot.')
        index = 0 
        for dinosaur in self.herd.dinosaurs:
            print(f'Press {index} for {dinosaur.name} with {dinosaur.health} health')
            index += 1


    def show_robot_opponent_options(self):
        print('Select your robot.')
        index = 0 
        for robot in self.fleet.robots:
            print(f'Press {index} for {robot.name} with {robot.health} health')

    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
            print('The Robots have won the game!')
        else:
            print('The Dinosaurs have won the game!')
