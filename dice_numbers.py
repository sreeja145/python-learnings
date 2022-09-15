import random


def dice():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


Dice = dice()
print(Dice)
