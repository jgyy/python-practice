"""
Change Return Program - The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters, dimes, nickels,
pennies needed for the change.
"""
import math


def greedy_money_exchange(denomination, amount):
    """
    :param denomination:
    :param amount:
    :return:
    """
    i = 0
    used = [0] * len(denomination)
    while amount > 0:  # go until all money gone
        # get num of that denomination to use, always round down
        num = math.floor(amount / denomination[i])
        used[i] = num  # say we've used it
        amount = amount - num * denomination[i]  # set new amount
        i += 1  # go to next denomination
    return used


if __name__ == '__main__':
    DENOMINATION = input("Enter Denomination: ")
    AMOUNT = int(input("Enter Amount: "))
    USED = greedy_money_exchange(DENOMINATION, AMOUNT)
    print(f"Used Amount: {USED}")
