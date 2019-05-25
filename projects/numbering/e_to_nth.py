""""Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go"""

from math import e


def e_with_precision(e_n):
    """Return euler's number to the n-th decimal place
    :param e_n: number of decimal places to return
    :type e_n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return '%.*f' % (e_n, e)


if __name__ == '__main__':
    # there is no do while loop in python, so we need to improvise
    CORRECT_INPUT = False
    PRECISION = 1
    while not CORRECT_INPUT:
        # ask until you get correct input
        print('Precision must be between 1 and 51')
        PRECISION = int(input('Number of decimal places: '))
        if 51 >= PRECISION > 0:
            CORRECT_INPUT = True
    print(e_with_precision(PRECISION))
