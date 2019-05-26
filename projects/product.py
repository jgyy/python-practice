"""
Product Inventory Project - Create an application which manages an inventory of products. Create
a product class which has a price, id, and quantity on hand. Then create an inventory class
which keeps track of various products and can sum up the inventory value.
"""
from abc import abstractmethod, ABCMeta


# noinspection PyCompatibility
class Entity(metaclass=ABCMeta):
    """Entity class"""
    @abstractmethod
    def id_number(self):
        """:return: 0"""
        return 0

    @staticmethod
    def default():
        """:return: False"""
        return False


class Product(Entity):
    """class documents"""
    id = 0

    def __init__(self, pro_name=None, value=0, amount=0, scale='kg'):
        """Constructor"""
        self._id = Product.id
        Product.id += 1
        if not pro_name:
            self._name = "{0}_{1}".format(self.__class__, self._id)
        else:
            self._name = pro_name
        self._value = value
        self._amount = amount
        self._scale = scale

    @property
    def id_number(self):
        """:return: id"""
        return self._id

    @property
    def name(self):
        """:return: name"""
        return self._name

    @property
    def value(self):
        """:return: value"""
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def amount(self):
        """:return: amount"""
        return self._amount

    @amount.setter
    def amount(self, other):
        self._amount = other

    @property
    def scale(self):
        """:return: scale"""
        return self._scale

    @scale.setter
    def scale(self, other):
        self._scale = other

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)

    def __str__(self):
        return "{amount}{scale} of {name} valued at {value}".format(
            amount=self._amount, scale=self._scale, name=self._name,
            value=self._value
        )


class Inventory(Entity):
    """Inventory class"""
    id = 0

    def __init__(self):
        self._id = Inventory.id
        Inventory.id += 1
        self._products = {}

    def product_add(self, *args):
        """:param args:"""
        def add_to_products(prod_add):
            """
            :param prod_add: if it's not a product it won't get added
            """
            try:
                self._products[prod_add.name].append(prod_add)
            except KeyError:
                self._products[prod_add.name] = [prod_add]

        for arg in args:
            if isinstance(arg, (tuple, list)):
                for prod in arg:
                    add_to_products(prod)
            elif isinstance(arg, Product):
                add_to_products(arg)

    @property
    def product_value(self):
        """
        :return: int: total value of product on hand
        """
        return sum(
            [single.value for prod in self._products for single in self._products[prod]])

    @property
    def product_count(self):
        """
        :return: int: amt of product on hand
        """
        return len([p for prod in self._products for p in self._products[prod]])

    @property
    def product_diff_amount(self):
        """
        :return: int: the amount of different products on hand
        """
        return len(self._products)

    @property
    def products(self):
        """
        :return: list(Product): product on hand
        """
        return self._products

    @property
    def id_number(self):
        """
        :return:  int: identity number of product
        """
        return self._id

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)


# noinspection PyCompatibility
class ObjFactory(metaclass=ABCMeta):
    """Object Factory Class"""

    def __init__(self):
        self._id = None

    @abstractmethod
    def get_object(self):
        """:return: 0"""
        return 0

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)


def gen_prod(value):
    """
    :param value: create an inventory
    :return: add some products to the inventory
    """
    return Product(value=value)


if __name__ == "__main__":
    INVENTORY = Inventory()
    for i in range(1, 10):
        INVENTORY.product_add(gen_prod(value=i))
    for i in range(1, 5):
        INVENTORY.product_add(gen_prod(value=i))
    # Get amount of product on hand, value of product, and amt of different product
    PROD_AMT = INVENTORY.product_count
    PROD_VAL = INVENTORY.product_value
    PROD_DIFF = INVENTORY.product_diff_amount
    for name, info in (("amount of product", PROD_AMT), ("value of product", PROD_VAL),
                       ("different products", PROD_DIFF)):
        print("{0}: {1}".format(name, info))
    print(INVENTORY.products)
    for product in INVENTORY.products:
        print(product + " prob details: " + str(INVENTORY.products[product]))
