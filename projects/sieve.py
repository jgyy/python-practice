"""
Sieve of Eratosthenes -
It is a simple, ancient algorithm
for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e. not prime),
the multiples of each prime, starting with the multiples of 2.
"""


def sieve(num):
    """
    :param num: stop at ``sqrt(n)``
    :return:
    """
    is_prime = [False] * 2 + [True] * (num - 1)
    for i in range(int(num ** 0.5 + 1.5)):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def main():
    """
    main function
    """
    try:
        num = int(input('Enter a number: '))
        print(sieve(num))
    except ValueError:
        print('Enter only an integer value, num > 1.')
        main()


if __name__ == '__main__':
    main()
