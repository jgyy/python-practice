import math
import string


def name_function():
    """
    DOCSTRING: Information about the function
    INPUT: no input...
    OUTPUT: Hello...
    :return:
    """
    print ( 'Hello' )


name_function ()


def say_hello(name_1='NAME'):
    print ( 'Hello ' + name_1 )


say_hello ( 'Sally' )


def add(n1, n2):
    return n1 + n2


print ( add ( 20, 30 ) )


def dog_check(my_string):
    """
    Find out if the word "dog" is in a string?
    :param my_string: Finds the word "dog"
    :return:
    """
    return 'dog' in my_string.lower ()


print ( dog_check ( 'Dog ran away' ) )


def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print ( pig_latin ( 'apple' ) )


def my_func(*args):
    for item in args:
        print ( item )
    # Returns 5% of the sum of a and b.
    return sum ( args ) * 0.05


print ( my_func ( 40, 60, 80, 100 ) )


def my_function(**kwargs):
    print ( kwargs )
    if 'fruit' in kwargs:
        print ( 'My fruit of choice is {}'.format ( kwargs['fruit'] ) )
    else:
        print ( 'I did not find any fruit here' )


my_function ( fruit='apple', veggie='lettuce' )


def my_functions(*args, **kwargs):
    print ( args, kwargs )
    print ( 'I would like {} {}'.format ( args[0], kwargs['food'] ) )


my_functions ( 10, 20, 30, fruit='orange', food='eggs', animal='dog' )


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min ( a, b )
    elif a % 2 != 0 or b % 2 != 0:
        return max ( a, b )


print ( lesser_of_two_evens ( 2, 5 ) )


def animal_crackers(text):
    t = text.lower ().split ()
    return t[0][0] == t[1][0]


print ( animal_crackers ( 'face food' ) )


def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


print ( makes_twenty ( 21, 10 ) )


def old_macdonald(name_2):
    first_half = name_2[:3].capitalize ()
    second_half = name_2[3:].capitalize ()
    return first_half + second_half


print ( old_macdonald ( 'te test' ) )


def master_yoda(text):
    word_list = text.split ()
    return " ".join ( word_list[::-1] )


print ( master_yoda ( 'we are men' ) )


def almost_there(n):
    return (abs ( 100 - n ) <= 10) or (abs ( 200 - n ) <= 10)


print ( almost_there ( 210 ) )


def has_33(nums):
    for i in range ( 0, len ( nums ) - 1 ):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


print ( has_33 ( [1, 3, 1, 3] ) )


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


print ( paper_doll ( 'test' ) )


def blackjack(a, b, c):
    cards = [a, b, c]
    if sum ( cards ) <= 21:
        return sum ( cards )
    elif 11 in cards and sum ( cards ) <= 31:
        return sum ( cards ) - 10
    else:
        return "BUST"


print ( blackjack ( 9, 9, 6 ) )


def summer_69(arr):
    total = 0
    addition = True
    for num in arr:
        while addition:
            if num != 6:
                total += num
                break
            else:
                addition = False
        while not addition:
            if num != 9:
                break
            else:
                addition = True
                break
    return total


print ( summer_69 ( [1, 2, 3, 4, 5, 6, 7, 8, 8, 9] ) )


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop ( 0 )
    return len ( code ) == 1


print ( spy_game ( [1, 2, 1, 3, 4, 5, 0, 7, 6] ) )


def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    xx = 3
    while xx <= num:
        for y in primes:
            if xx % y == 0:
                xx += 2
                break
        else:
            primes.append ( xx )
            xx += 2
    print ( primes, len ( primes ) )
    return len ( primes )


count_primes ( 111 )


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *',
                4: '*****', 5: '**** ', 6: '   * ',
                7: ' *   ', 8: '*  * ', 9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5],
                'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper ()]:
        print ( patterns[pattern] )


print_big ( 'a' )
my_nums = [1, 2, 3, 4, 5]
print ( list ( map ( lambda num: num ** 2, my_nums ) ) )


def splicer(my_string):
    if len ( my_string ) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Andy', 'Eve', 'Sally']
print ( list ( map ( splicer, names ) ) )
my_numbers = [1, 2, 3, 4, 5, 6]
print ( list ( filter ( lambda num: num % 2 == 0, my_nums ) ) )
print ( list ( map ( lambda ex: ex[::-1], names ) ) )
x = 25


def printer():
    y = 50
    return y


print ( x, printer () )
name = 'THIS IS A GLOBAL STRING'


def greet():
    naming = 'Sammy'

    def hello():
        print ( 'Hello ' + naming )

    hello ()


greet ()


def func(xx):
    print ( f'X is {xx}' )
    xx = 'NEW VALUE'
    print ( f'I JUST LOCALLY CHANGED X to {xx}' )
    return xx


print ( func ( x ) )


def vol(rad):
    return (4 / 3) * math.pi * (rad ** 3)


def ran_check(num, low, high):
    if num in range(low, high):
        print('The number is within range')
    elif num < low:
        print('The number is below range')
    elif num > high:
        print('The number is above range')
    return num in range(low, high)


print(vol(10), ran_check(1, 2, 3))


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for character in s:
        if character.isupper():
            d["upper"] += 1
        elif character.islower():
            d["lower"] += 1
    return "No. of Upper case characters : {}\nNo. of Lower case characters : {}".format(d["upper"], d["lower"])


print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))


def unique_list(l):
    ul = []
    for single in l:
        if single not in ul:
            ul.append(single)
    return ul


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 4, 3, 2, 1]))


def multiply(numbers):
    answer = 1
    for multi in numbers:
        answer *= multi
    return answer


print(multiply([1, 2, 3, -4, 5]))


def palindrome(s):
    str_filter = s.replace(" ", "")
    return str_filter == str_filter[::-1]


print(palindrome("nurses running"))


def is_pang(str1, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(str1.lower())


print(is_pang("The quick brown fox jumps over the lazy dog"))
