"""
Find PI to the Nth Digit
Have the user enter a number 'n'
and print out PI to the 'n'th digit
"""


def calc_pi(limit):
    """
    Generator function
    Prints out the digits of PI
    until it reaches the given limit
    """

    calc_q, calc_r, calc_t, calc_k, calc_n, calc_l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * calc_q + calc_r - calc_t < calc_n * calc_t:
            # yield digit
            yield calc_n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            n_r = 10 * (calc_r - calc_n * calc_t)
            calc_n = ((10 * (3 * calc_q + calc_r)) // calc_t) - 10 * calc_n
            calc_q *= 10
            calc_r = n_r
        else:
            n_r = (2 * calc_q + calc_r) * calc_l
            n_n = (calc_q * (7 * calc_k) + 2 + (calc_r * calc_l)) // (calc_t * calc_l)
            calc_q *= calc_k
            calc_t *= calc_l
            calc_l += 2
            calc_k += 1
            calc_n = n_n
            calc_r = n_r


def main():
    """
    Wrapper function
    Calls CalcPi with the given limit
    """
    pi_digits = calc_pi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for pi_d in pi_digits:
        print(pi_d, end='')
        i += 1
        if i == 40:
            print("")
            i = 0


if __name__ == '__main__':
    main()
