"""Practice on Object Oriented Programming"""
import math


class Animal:
    """Parent Class on inheritance and polymorphism"""
    animal = "Animal: "

    def __init__(self, name):
        self.name = name
        print("ANIMAL CREATED")

    def who_am_i(self):
        """Stating the animal identity"""
        print(self.animal + "I am an animal")

    def eat(self):
        """Commenting on consumption status"""
        print(self.animal + "I am eating")

    def speak(self):
        """Implement this in the sub class"""
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    """
    CLASS OBJECT ATTRIBUTE
    SAME FOR ANY INSTANCE OF A CLASS
    """
    species = 'mammal'

    def __init__(self, breed, name):
        Animal.__init__(self, name)
        self.breed = breed
        self.name = name
        print("Dog Created")

    def who_am_i(self):
        """Overwrite the function from animal class"""
        print("I am a dog!")

    def bark(self, number):
        """Narrating a barking dog"""
        print(f"{self.name} number {number} is barking, WOOF!")

    def eat(self):
        """Commenting on consumption status"""
        print("I am a dog and eating")

    def speak(self):
        """
        :return: returns the narrating string
        """
        return self.name + " says woof!"


class Cat:
    """Setting up cat object"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        :return: Narrating the meow string
        """
        return self.name + " says meow!"


class Circle:
    """Another class object attribute and method"""
    pi = math.pi

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius ** 2 * self.pi

    def get_circumference(self):
        """:return: Returning the circumference of the circle"""
        return self.radius * self.pi * 2


class Book:
    """Stating book parameters"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted.")


class Line:
    """Tabulates distance and slope"""

    def __init__(self, coordinate1, coordinate2):
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def distance(self):
        """Calculate the line distance"""
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        """Calculates the line slope"""
        return (self.y2 - self.y1) / (self.x2 - self.x1)


class Cylinder:
    """Container object for cylinder"""

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        """Calculate the cylinder volume"""
        return self.height * math.pi * self.radius ** 2

    def surface_area(self):
        """Calculate the surface area"""
        top = math.pi * self.radius ** 2
        return (2 * top) + (2 * math.pi * self.radius * self.height)


class Account:
    """Bank account class"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

    def deposit(self, amount):
        """Calculation to deposit money"""
        self.balance += amount
        print(f"We just added {amount} to the balance")

    def withdraw(self, amount):
        """Calculation to withdraw money"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"We just withdraw {amount} to the balance")
        else:
            print("Sorry not enough funds!")


class Simple:
    """A simple class"""

    def __init__(self, value):
        self.value = value

    def add_to_value(self, amount):
        """:param amount: adding amount to value"""
        self.value += amount
        print(f"We just added {amount} to your value")


my_dog = Dog(breed = 'lab', name = 'Sammy')
my_dog.bark(1)
my_dog.who_am_i()
my_dog.eat()
print(my_dog.breed, my_dog.name, my_dog.species)
my_circle = Circle(30)
print(my_circle.pi, my_circle.radius, my_circle.area, my_circle.get_circumference())
my_animal = Animal("dog")
my_animal.who_am_i()
my_animal.eat()
niko = Dog("breed", "niko")
felix = Cat("felix")
for pet in [niko, felix]:
    print(type(pet), pet.speak())


def pet_speak(pets):
    """:param pets: placeholder for different pets"""
    print(pets.speak())


pet_speak(niko)
pet_speak(felix)
fido = Dog("a", "Fido")
isis = Cat("Isis")
print(fido.speak(), isis.speak())
b = Book('Python rocks', 'Jose', 200)
print(b, len(b))
del b
c1 = (3, 2)
c2 = (8, 10)
li = Line(c1, c2)
print(li.distance(), li.slope())
c = Cylinder(2, 3)
print(c.volume(), c.surface_area())
acct1 = Account('Jose', 100)
acct1.deposit(100)
acct1.withdraw(10)
print(acct1, acct1.owner, acct1.balance)
my_obj = Simple(300)
my_obj.add_to_value(500)
print(my_obj.value)
