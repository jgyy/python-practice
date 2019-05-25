"""
Program takes an integer as an input and returns the word representation of the integer.
Works up to 999,999,999
Program begins by parsing number to array of digits with numToArray method
"""

UNITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
         'seventeen', 'eighteen', 'nineteen']
TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
PLACES = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
          'seventh', 'eighth', 'ninth']
TEEN_PLACES = ['tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth',
               'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
TENS_PLACES = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth',
               'sixtieth', 'seventieth', 'eightieth', 'ninetieth']


def num_to_array(num):
    """
    :param num:
    :return:
    """
    num_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_array[0] = int(num/100000000) % 10  # Hundred Millions place
    num_array[1] = int(num/10000000) % 10  # Ten Millions place
    num_array[2] = int(num/1000000) % 10  # Millions place
    num_array[3] = int(num/100000) % 10  # Hundred-thousands place
    num_array[4] = int(num/10000) % 10  # Ten-thousands place
    num_array[5] = int(num/1000) % 10  # Thousands place
    num_array[6] = int(num/100) % 10  # Hundreds place
    num_array[7] = int(num/10) % 10  # Tens place
    num_array[8] = num % 10  # Ones place
    return num_array


def has_trailing_zeros(num_array):
    """
    :param num_array:
    :return:
    """
    condition = False
    if num_array[6] != 0:
        condition = num_array[7] == 0 and num_array[8] == 0
    elif num_array[3] != 0 or num_array[4] != 0 or num_array[5] != 0:
        condition = num_array[6] == 0 and num_array[7] == 0 and num_array[8] == 0
    elif num_array[0] != 0 or num_array[1] != 0 or num_array[2] != 0:
        condition = num_array[3] == 0 and num_array[4] == 0 and num_array[5] == 0 \
                    and num_array[6] == 0 and num_array[7] == 0 and num_array[8] == 0
    return condition


def num_to_words(num):
    """
    :param num:
    :return:
    """
    num_array = num_to_array(num)
    word = ''
    if num == 0:
        word = 'zero'
    if 1 <= num <= 9:
        word = UNITS[num]
    if 10 <= num <= 19:
        word = TEENS[num % 10]
    if 20 <= num <= 99:
        word += TENS[int(num/10)]
        if num_array[8] != 0:
            word += ' ' + UNITS[num % 10]

    if 100 <= num <= 999:
        word += UNITS[num_array[6]] + ' hundred '
        if not has_trailing_zeros(num_array):
            word += num_to_words(num_array[7] * 10 + num_array[8])

    if 1000 <= num <= 999999:
        word += num_to_words(num_array[3] * 100 +
                             num_array[4] * 10 + num_array[5]) + ' thousand '
        if not has_trailing_zeros(num_array):
            word += num_to_words(num_array[6] * 100 + num_array[7] * 10 + num_array[8])

    if 1000000 <= num <= 999999999:
        word += num_to_words(num_array[0] * 100 +
                             num_array[1] * 10 + num_array[2]) + ' million '
        if not has_trailing_zeros(num_array):
            word += num_to_words(
                num_array[3] * 100000 + num_array[4] * 10000 +
                num_array[5] * 1000 + num_array[6] * 100 +
                num_array[7] * 10 + num_array[8])

    word = ' '.join(word.split())
    return word


def num_to_place(num):
    """
    :param num:
    :return:
    """
    num_array = num_to_array(num)
    place = ''
    if num == 0:
        place += 'zeroth'
    if 1 <= num <= 9:
        place += PLACES[num]
    if 10 <= num <= 19:
        place += TEEN_PLACES[num % 10]
    if 20 <= num <= 99:
        if num_array[8] == 0:
            place += TENS_PLACES[int(num/10)]
        else:
            place += TENS[int(num/10)] + ' ' + PLACES[num % 10]

    if 100 <= num <= 999:
        if has_trailing_zeros(num_array):
            place += UNITS[num_array[6]] + ' hundredth'
        else:
            place += UNITS[num_array[6]] + ' hundred ' +\
                     num_to_place(num_array[7] * 10 + num_array[8])

    if num >= 1000:
        place = num_over_1000(num, num_array, place)
    place = ' '.join(place.split())
    return place


def num_over_1000(num, num_array, place):
    """
    :param num:
    :param num_array:
    :param place:
    :return:
    """
    if 1000 <= num <= 999999:
        if has_trailing_zeros(num_array):
            place += num_to_words(num_array[3] * 100 +
                                  num_array[4] * 10 + num_array[5]) + ' thousandth'
        else:
            place += num_to_words(num_array[3] * 100 +
                                  num_array[4] * 10 + num_array[5]) + ' thousand '
            if not has_trailing_zeros(num_array):
                place += num_to_place(num_array[6] * 100 + num_array[7] * 10 + num_array[8])

    if 1000000 <= num <= 999999999:
        if has_trailing_zeros(num_array):
            place += num_to_words(num_array[0] * 100 +
                                  num_array[1] * 10 + num_array[2]) + ' millionth'
        else:
            place += num_to_words(num_array[0] * 100 +
                                  num_array[1] * 10 + num_array[2]) + ' million '
            if not has_trailing_zeros(num_array):
                place += num_to_place(
                    num_array[3] * 100000 + num_array[4] * 10000 +
                    num_array[5] * 1000 + num_array[6] * 100 + num_array[7] * 10 + num_array[8])
    return place


def main():
    """Run the main script"""
    number = input('Please enter a number: ')
    if number != '':
        print('Word:\t%s' % num_to_words(int(number)))
        print('Place:\t%s' % num_to_place(int(number)))
    if number[0].lower() != 'q':
        main()


if __name__ == "__main__":
    main()
