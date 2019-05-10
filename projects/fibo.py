"""
Fibonacci Sequence Generator
Have the user enter a number and
generate a fibonacci sequence
which size is equivalent to that number.
"""


def fib_sequence(num):
    """
    Generates a fibonacci sequence
    with the size of n
    """
    assert num > 0

    series = [1]

    while len(series) < num:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in enumerate(series):  # Convert the numbers to strings
        series[i[0]] = str(series[i[0]])

    return ', '.join(series)  # Return the sequence separated by commas


def main():
    """Wrapper function"""
    print(fib_sequence(int(input('How many numbers do you need? '))))


if __name__ == '__main__':
    main()
