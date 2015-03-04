import random

class Position:
    def __init__(self, x=0, y=0, rand=False):
        self.x = x
        self.y = y

        if rand == True:
            self.randomize()

    def randomize(self):
        self.x = random.randint(0,4)
        self.y = random.randint(0,4)
