from __future__ import print_function
import string
from position import Position
import personnel

class EncounteredEvilRobot(IndexError):
    '''This is raise when the player hits an EvilRobot'''
    def __init__(self, message, charac):
        super(EncounteredEvilRobot, self).__init__(message)

        self.charac = charac

class EncounteredRatTrap(IndexError):
    '''This is raise when the player hits a Rat Trap'''

class EncounteredBackpack(IndexError):
    '''This is raise when the player hits the Backpack'''

class Backpack:
    def __init__(self):
        self.pos = Position(rand=True)
        self.sym = 'B'

class RatTrap:
    def __init__(self):
        self.pos = Position(rand=True)
        self.sym = 'R'

class Game:
    backpack = Backpack()
    rattrap = RatTrap()

    intro = "It's a dark and stormy night. One unfortunate Computer Science\n"
    intro += "student has fallen asleep on the Love 105 suites couch while\n"
    intro += "cramming for their upcoming final. They head down to the Majors\n"
    intro += "Lab to gather their belongings before heading home. They\n"
    intro += "approach the lab and encounter a strange sight: the lab is empty\n"
    intro += "and dark...but the door is open. The power must have been knocked\n"
    intro += "out by the storm. The brave little CS student enters the dark room\n"
    intro += "to find their backpack..."

    def __init__(self, player):
        self.grid = [['+' for x in range(5)] for x in range(5)]
        print(self.intro)

        self.player = player
        self.opponent = None

        self.over = False
        self.init_grid()

    def init_grid(self):
        self.place_item(self.player)
        self.place_item(self.backpack)
        self.place_item(self.rattrap)

        for i in range(4):
            self.place_item( personnel.EvilRobot() )

    def place_item(self, item):
        good = False

        while not good:
            if self.grid[ item.pos.y ][ item.pos.x ] == '+':
                self.grid[ item.pos.y ][ item.pos.x ] = item
                good = True
            else:
                item.pos = Position(rand=True)

    def place_player_and_check(self, pos):
        if pos.x < 0 or pos.y < 0:
            raise IndexError('{} has run into a wall. Try another direction'.format(
                                self.player.name))
        elif self.grid[ pos.y ][ pos.x ] == '+':
            self.grid[ pos.y ][ pos.x ] = self.player
            self.grid[ self.player.pos.y ][ self.player.pos.x ] = '+'
            self.player.pos.x = pos.x
            self.player.pos.y = pos.y
        elif self.grid[ pos.y ][ pos.x ].sym == 'E':
            error = '{} has encountered an Evil Robot. It appears to have\n'.format(
                        self.player.name)
            error += 'assembled itself out of spare parts. Prepare to fight!\n'
            raise EncounteredEvilRobot( error, self.grid[ pos.y ][ pos.x ] )
        elif self.grid[ pos.y ][ pos.x ].sym == 'R':
            error = '{} rand into one of those legendary mecahnical rat\n'.format(
                        self.player.name)
            error += 'traps in the Love basement. RIP.\n'
            raise EncounteredRatTrap(error)
        elif self.grid[ pos.y ][ pos.x ].sym == 'B':
            success = 'Congratulations, {} found their backpack!!!'.format(
                        self.player.name)
            raise EncounteredBackpack(success)
        else:
            raise IndexError('{} has run into a wall. Try another direction'.format(
                                self.player.name))

    def move_player(self, direc):
        if self.opponent == None:
            if direc == 'n':
                x = self.player.pos.x
                y = self.player.pos.y - 1
                pos = Position(x, y)
            elif direc == 's':
                x = self.player.pos.x
                y = self.player.pos.y + 1
                pos = Position(x, y)
            elif direc == 'e':
                x = self.player.pos.x + 1
                y = self.player.pos.y
                pos = Position(x, y)
            elif direc == 'w':
                x = self.player.pos.x - 1
                y = self.player.pos.y
                pos = Position(x, y)

            try:
                self.place_player_and_check(pos)
            except EncounteredEvilRobot as e:
                print(e)
                self.opponent = e.charac
            except EncounteredRatTrap as e:
                print(e)
                self.over = True
            except EncounteredBackpack as success:
                print(success)
                win_message = 'And so, our hero safely makes their way to the exit. Luckily, {} made it out\n'.format(
                                self.player.name)
                win_message += 'alive this time. But one thing is for sure: {} will never put off studying for\n'.format(
                                self.player.name)
                win_message += 'for their final exams ever again.\n'
                print(win_message)
                self.over = True
            except IndexError as e:
                print(e)
        else:
            print('{} can\'t run from the Evil Robot.'.format(self.player.name))

    def fight(self):
        if self.opponent != None:
            self.opponent = self.player.attack(self.opponent)
            self.check_for_winner()
            if self.opponent != None:
                self.player = self.opponent.attack(self.player)
                self.check_for_winner()
        else:
            print('{} doesn\'t see anything worth attacking.'.format(self.player.name))

    def check_for_winner(self):
        if self.player.hp <= 0:
            print('{}\'s epic backpack search has come to an end. RIP')
            self.over = True
        elif self.opponent.hp <= 0:
            print('Evil Robot has crashed! {} wins!'.format(self.player.name))
            self.grid[ self.opponent.pos.y ][ self.opponent.pos.x ] = self.player
            self.grid[ self.player.pos.y ][ self.player.pos.x ] = '+'
            self.player.pos.x = self.opponent.pos.x
            self.player.pos.y = self.opponent.pos.y
            self.opponent = None

    def print_grid(self):
        for r in self.grid:
            for c in r:
                if c != '+':
                    print(c.sym, ' ', end='')
                else:
                    print(c, ' ', end='')
            print()
