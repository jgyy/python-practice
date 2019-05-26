"""
problem description: program to find the factorial values of numbering
for some given number of inputs
"""


def fac(num):
    """
    :param num:
    :return:
    """
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * fac(num - 1)


if __name__ == "__main__":
    T = int(input("While loop repeat count: "))
    while T:
        T -= 1
        N = int(input("Type a number here: "))
        P = fac(N)
        print("The factorial values are: " + str(P))
