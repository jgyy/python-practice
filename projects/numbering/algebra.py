"""
Complex Number Algebra - Show addition, multiplication, negation,
and inversion of complex numbering in separate functions.
(Subtraction and division operations can be made with pairs of these operations.)
Print the results for each operation tested.
"""
from math import sqrt


class Complex:
    """Complex Class"""

    def __init__(self, x, y):
        self.x_num = x
        self.y_num = y

    def add(self):
        """
        :return:
        """
        return Number(self.x_num.real + self.y_num.real,
                      self.x_num.imaginary + self.y_num.imaginary).show()

    def multi(self):
        """
        :return:
        """
        return Number(self.x_num.real * self.y_num.real -
                      self.x_num.imaginary * self.y_num.imaginary,
                      self.y_num.real * self.x_num.imaginary +
                      self.x_num.real * self.y_num.imaginary).show()


class Number:
    """Number class"""

    def __init__(self, x, y):
        self.real = x
        self.imaginary = y

    def show(self):
        """Static print statement"""
        print(self.real, self.imaginary)

    def negation(self):
        """
        :return:
        """
        self.real *= -1
        self.imaginary *= -1
        return self

    def inversion(self):
        """
        :return:
        """
        root = sqrt(self.real * self.real + self.imaginary * self.imaginary)
        self.real = (self.real / root)
        self.imaginary = -(self.imaginary / root)
        return self


if __name__ == "__main__":
    N1 = Number(3, 2)
    N2 = Number(1, 1)

    N1.negation().show()
    N1.inversion().show()

    C = Complex(N1, N2)

    C.add()

    C.multi()
