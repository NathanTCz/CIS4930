from __future__ import print_function
from random import *
from position import Position

class Character:
    def __init__(self):
        self.pos = Position(0, 2)

    def attack(self, opp):
        return self.calc_damage(opp)

    def calc_damage(self, opponent):
        damage = randint(0, 6) + self.strength - opponent.defense
        if damage <= 0:
            print("{} evades {}'s attack.".format(opponent.name, self.name))
        else:
            opponent.hp = opponent.hp - damage
            print("{} attacks {} for {} points of damage!".format(
                            self.name, opponent.name, str(damage)))

        return opponent

class EvilRobot(Character):
    def __init__(self):
        Character.__init__(self)
        self.hp = 15
        self.name = 'Evil Robot'
        self.strength = 9
        self.defense = 7
        self.sym = 'E'

class Player(Character):
    def __init__(self, n):
        Character.__init__(self)
        self.hp = 30
        self.name = n
        self.sym = 'P'

    def help(self):
        print('go [N, S, E, or W]')
        print('quit')
        print('attack')
        print('health')
        print('help')

    def health(self):
        print(self.name, 'has', self.hp,'HP.')

    def go(self):
        pass

    def quit(self):
        print(self.name, 'has lost all hope and locked themself in the ACM office')
        print('to read ancient ACM magazines and await their final doom.')


class CodeWarrior(Player):
    def __init__(self, n):
        Player.__init__(self, n)
        self.strength = 10
        self.defense = 8

class Hax0r(Player):
    def __init__(self, n):
        Player.__init__(self, n)
        self.strength = 8
        self.defense = 10
