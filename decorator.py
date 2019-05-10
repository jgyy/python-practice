"""Decorator Script"""


def func():
    """:return: returns one"""
    return 1


def hello(name='Jose'):
    """Parent function"""
    print("The hello() function has been executed!")

    def greet():
        """:return: returning a hello string"""
        return "\t This is the greet() func inside hello, " + name + "\n"

    def welcome():
        """:return: returning a welcome string"""
        return '\t This is welcome() inside hello\n'

    print("I am going to return a function!")

    if name == 'Jose':
        return greet()
    return welcome()


def cool():
    """:return: return super cool function"""
    def super_cool():
        """:return: return cool function text"""
        return 'I am very cool!\n'

    return super_cool()


def other(some_def_func):
    """Print out other function"""
    print("Other code runs here!\n")
    print(some_def_func())


def new_decorator(original_func):
    """
    :param original_func: takes in the function
    :return: return function
    """
    def wrap_func():
        """Wrap function with function"""
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function!')
    return wrap_func


@new_decorator
def func_needs_decorator():
    """Side effect print text"""
    print("I want to be decorated!!\n")


print(func())
func_needs_decorator()
