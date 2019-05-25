"""
Coin Flip Simulation - Write some code that simulates flipping
a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.
"""
import random


def flip():
    """
    :return:
    """
    flipping = random.random()
    return flipping >= .5


def main(num):
    """
    :param num:
    """
    heads = 0
    tails = 0
    result_string = ""

    for _ in range(int(num)):
        if flip():
            heads += 1
            result_string += "H"
        else:
            tails += 1
            result_string += "T"

    print("Number of Heads: %i" % heads)
    print("Number of Tails: %i" % tails)
    print(result_string)


if __name__ == '__main__':
    USER_INPUT = input("Please enter a number of flips: ")
    main(USER_INPUT)
