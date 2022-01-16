import random

randomizer = random.randint(1, 2)


def head_tail(n):
    if n == 1:
        print("Heads")
    else:
        print("Tails")


head_tail(randomizer)
