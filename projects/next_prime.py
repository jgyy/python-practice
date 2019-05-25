"""
Next Prime Number
Generate prime numbering until
the user chooses to stop
"""


def is_prime(num_x):
    """
    Checks whether the given
    number x is prime or not
    """

    if num_x == 2:
        return True

    if num_x % 2 == 0:
        return False

    for i in range(3, int(num_x ** 0.5) + 1, 2):
        if num_x % i == 0:
            return False

    return True


def gen_prime(current_prime):
    """
    Returns the next prime
    after the currentPrime
    """

    new_prime = current_prime + 1

    while True:

        if not is_prime(new_prime):
            new_prime += 1
        else:
            break

    return new_prime


def main():
    """Wrapper function"""
    current_prime = 2

    while True:
        answer = input('Would you like to see the next prime? (Y/N) ')

        if answer.lower().startswith('y'):
            print(current_prime)
            current_prime = gen_prime(current_prime)
        else:
            break


if __name__ == '__main__':
    main()
