"""
Calculator- Have the user enter 2 number - a. b - and an operator - op - and calculate
the solution - c - according to the type of the given operator
"""


def calc(num_a, num_b, operator):
    """
    Returns a string like this: a op b = c
    where c is the computed value according to the operator
    """
    expression = str(num_a) + ' ' + operator + ' ' + str(num_b) + ' = '
    result = ''
    if operator not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'
    if operator == '+':
        result = str(num_a + num_b)
    elif operator == '-':
        result = str(num_a - num_b)
    elif operator == '*':
        result = str(num_a * num_b)
    elif operator == '/':
        result = str(num_a / num_b)
    return expression + result


def main():
    """Wrapper function"""
    num_a = int(input('Please type the first number: '))
    num_b = int(input('Please type the second number: '))
    operator = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    print(calc(num_a, num_b, operator))


if __name__ == '__main__':
    main()
