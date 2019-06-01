"""GUI"""
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


def func(x):
    """
    :param x:
    :return:
    """
    return x


if __name__ == '__main__':
    interact(func, x=10)
