"""
Enter two numbering a and b (separated by newline)
and the program will print a^b with O(log N) time complexity
"""


def power(input_a, input_b):
    """
    Return a to the power of b
    """
    if input_b == 0:
        return 1
    temp = power(input_a, int(input_b / 2))
    if input_b % 2 == 0:
        return temp * temp
    return temp * temp * input_a


if __name__ == '__main__':
    INPUT_A = int(input("Please enter the initial integer: "))
    INPUT_B = int(input("Please enter the power factor: "))
    print(power(INPUT_A, INPUT_B))
