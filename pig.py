import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randin(min_value, max_value)

    return roll 

value = roll()
print(value)