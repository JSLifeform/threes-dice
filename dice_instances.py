#threes dice game

#import random for dice rolling
import random

#initialize generic die
class Die:
    def __init__(self, sides = 6, value = 0):
        if sides < 2:
            raise ValueError("Must have at least 2 sides to randomize die!")
        if isinstance(sides, int):
            raise ValueError("The number of sides of a die must be an integer, silly goose!")
        self.value = value or random.randint(1, sides)



#initialize d6 class
class D6(Die):
    def __init__(self):
        super.__init__(sides = 6,  value = value)

test = D6()