"""Practice on error handling"""


def add(n_1, n_2):
    """
    :param n_1: first number
    :param n_2: second number
    """
    print(n_1 + n_2)


def my_func():
    """A simple function"""
    first, second = 1, 2
    print(first, second)


try:
    RESULT = 10 + 10
    add(10, 20)
except TypeError:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(RESULT)

try:
    F = open('testfile')
    F.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey, you have an OS Error")
finally:
    print("I always run")


def ask_for_int():
    """Seek a number from the user"""
    while True:
        try:
            results = int(input("Please provide number: "))
        except ValueError:
            print("Whoops! That is not a number \n")
            continue
        else:
            print(f"Thank you, your number squared is: {results ** 2}")
            break


ask_for_int()
try:
    for i in ['a', 'b', 'c', 1]:
        print(i ** 2)
except TypeError:
    print("Type error! Watch out!")
try:
    X, Y = 5, 0
    Z = X / Y
except ZeroDivisionError:
    print("Zero Division Error!")
finally:
    print("All Done")
my_func()
