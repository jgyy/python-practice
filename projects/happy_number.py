"""Happy Numbers"""


def get_digits(number):
    """
    :param number:
    :return:
    """
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits


def is_happy_number(number):
    """
    :param number:
    :return:
    """
    previous_numbers = []
    while True:
        digits = get_digits(number)
        sum_of_squared_digits = sum(list(map(lambda x: x ** 2, digits)))
        if sum_of_squared_digits == 1:
            return True
        if sum_of_squared_digits in previous_numbers:
            return False
        number = sum_of_squared_digits
        previous_numbers.append(number)


def print_happy_number(number):
    """
    :param number:
    :return:
    """
    happy_numbers = []
    count = 0
    while count < 8:
        if is_happy_number(number):
            happy_numbers.append(number)
            count += 1
        number += 1
    return happy_numbers


if __name__ == "__main__":
    NUMBER = input("Please enter a number: ")
    print(print_happy_number(int(NUMBER)))
