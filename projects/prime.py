"""
Prime Factorization - Have the user enter a number
and find all Prime Factors (if there are any) and display them.
"""


def factors(num):
    """
    :param num:
    :return:
    """
    for num_x in range(1, num + 1):
        if not num % num_x:
            yield num_x


def is_prime(num):
    """
    :param num:
    :return:
    """
    return len(list(factors(num))) == 2


def prime_factors(num):
    """
    :param num:
    :return:
    """
    return list(filter(is_prime, list(factors(num))))


def prime_factorize(number):
    """
    :param number:
    :return:
    """
    number = int(number)
    number_f = prime_factors(number)
    if is_prime(number):
        return str(number)
    return str(number_f[0]) + "*" + prime_factorize(number / number_f[0])


if __name__ == '__main__':
    print("Welcome to the Prime Factorization.. "
          "Enter the numbering in the prompt or enter 'quit' to exit")
    NUM = 0

    while True:
        if NUM:
            print(prime_factorize(NUM))
        NUM = input(">>> ")
        if NUM == "quit":
            break
