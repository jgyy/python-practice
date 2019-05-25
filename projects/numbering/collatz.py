"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps
it takes to reach one using the following process: If n is even, divide
it by 2. If n is odd, multiply it by 3 and add 1.
"""


def collatz_recur(cur_num, count=0):
    """This recursively solves the Collatz Conjecture"""
    if cur_num <= 1:  # Base case
        return count
    if cur_num % 2 == 0:
        return collatz_recur(cur_num / 2, count + 1)
    return collatz_recur(cur_num * 3 + 1, count + 1)


if __name__ == '__main__':
    COUNT = 0
    while COUNT < 9999:
        # Some tests
        print("The current number is: ", collatz_recur(COUNT+2))  # 1
        print("The current number is: ", collatz_recur(COUNT+3))  # 7
        print("The current number is: ", collatz_recur(COUNT+4))  # 2
        print("The current number is: ", collatz_recur(COUNT+5))  # 5
        print("The current number is: ", collatz_recur(COUNT+6))  # 8
        COUNT += 1
