"""
problem description: program to find the factorial values of numbers
for some given number of inputs
"""


def fac(n):
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return n * fac(n - 1)


t = input()
while (t):
    t = t - 1
    n = input()
    p = fac(n)
    print
    p