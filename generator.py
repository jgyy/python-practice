"""Generator Script"""
import random


def create_cubes(num):
    """
    :param num: number
    """
    for cube_x in range(num):
        yield cube_x ** 3


def gen_fib(num):
    """:param num: number range"""
    num_a, num_b = 1, 1
    for _ in range(num):
        yield num_a
        num_a, num_b = num_b, num_a + num_b


def simple_gen():
    """yield count 1 by 1"""
    for num_x in range(11):
        yield num_x


def gen_squares(num):
    """:param num: number"""
    for square in range(num):
        yield square**2


def rand_num(low, high, num):
    """
    :param low: lowest number
    :param high: highest number
    :param num: total numbering to iterate
    """
    for _ in range(num):
        yield random.randint(low, high)


print(list(create_cubes(11)))
print(list(gen_fib(11)))
print(list(simple_gen()))
G = simple_gen()
print(next(G), next(G), next(G), next(G))
S = "hello world"
S_ITER = iter(S)
print(next(S_ITER), next(S_ITER), next(S_ITER), next(S_ITER))
print(list(gen_squares(11)))
print(list(rand_num(1, 11, 22)))
MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
GEN_COMPUTE = (item for item in MY_LIST if item > 3)
print(list(GEN_COMPUTE))
