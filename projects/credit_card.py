"""
Credit Card Validator - Takes in a credit card number from a common
credit card vendor (Visa, MasterCard, American Express, Discover) and
validates it to make sure that it is a valid number (look into how
credit cards use a checksum).
"""


def val_cc(number):
    """
    :param number:
    :return:
    """
    cc_rev = number[::-1]
    total = 0
    for i in cc_rev[1::2]:
        num_x = int(i) * 2
        if len(str(num_x)) == 2:
            for num_a in str(num_x):
                total += int(num_a)
        else:
            total += int(num_x)

    for i in cc_rev[::2]:
        total += int(i)

    return total


def credit_card():
    """credit card"""
    if val_cc(CC) % 10 == 0:
        print("%s is a valid credit card number" % CC)
    else:
        print("%s is NOT a valid credit card number" % CC)


if __name__ == '__main__':
    CC = str(input("Enter a credit card number to validate "
                   "(Mastercard, Visa, Discover, Amex only): "))
    if 51 <= int(CC[:2]) <= 55 and len(CC) == 16:
        credit_card()
    elif int(CC[0]) == 4 and (len(CC) == 13 or len(CC) == 16):
        credit_card()
    elif (int(CC[:2]) == 34 or int(CC[:2]) == 37) and len(CC) == 15:
        credit_card()
    elif int(CC[:4]) == 6011 and len(CC) == 16:
        credit_card()
    else:
        print("%s is NOT a valid credit card number" % CC)
