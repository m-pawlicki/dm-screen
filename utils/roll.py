import random

def roll(self, number, sides, modifier = 0):
    if number <= 0 or sides <= 0:
        raise Exception("Number of dice or sides can\'t be negative!")
    dice = [random.randint(1, sides) for _ in range(number)]
    sub = sum(dice)
    total = sub + modifier
    return total