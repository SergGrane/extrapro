# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers. They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will
# form orders from customers.
import abc
from abc import ABC, abstractmethod


class Pizza(abc.ABC):
    """
    Abstract class of pizza
    """

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Ingredients:
    """
    describes extra ingredients to the pizza
    """

    def __init__(self, name: str, price: float):
        """
        constructor of ingredients class
        :param name:
        :param price:
        """
        if not isinstance(price, (int, float)) or not isinstance(name, str):
            raise TypeError('Price or name is wrong type')
        self.price = price
        self.name = name

    def __str__(self):
        return 'Xtra ingredient: ' + self.name + ', Price: ' + str(self.price) + ' UAH'


class PizzaoftheDay (Pizza):

    """
     describes pizza-of-the-day for business lunch
    """

    def __init__(self, name: str, base_price: float):
        """
        constructor of Pizzaoftheday class
        :param name:
        :param base_price:
        """
        super().__init__(name, base_price)
        self.__adds = []

    def add_xtraingredient(self, xtra_ingr: Ingredients):
        """
        adding of xtraingredien to pizza
        :param xtra_ingr:
        :return:
        """
        if not isinstance(xtra_ingr, Ingredients):
            raise TypeError('Ingredient does not exist!')
        self.__adds.append(xtra_ingr)

    def total_price(self):
        """
        calculating the total price of pizza
        :return:
        """
        s = self.price
        for item in self.__adds:
            s += item.price
        return s

    def __str__(self):
        res = '\n'.join(map(str, self.__adds))
        return f'{self.name}, Base price: {self.price} UAH\n{res} \n\tTotal price: {self.total_price()} UAH '


if __name__ == '__main__':
    try:
        ing1 = Ingredients('Salami', 22.0)
        print(ing1)
        ing2 = Ingredients('Mushrooms', 25.0)
        print(ing2)
        ing3 = Ingredients('Olives', 18.0)
        print(ing3)
        sunday = PizzaoftheDay('Salami pizza', 120.0)
        sunday.add_xtraingredient(ing2)
        sunday.add_xtraingredient(ing3)
        print(sunday)

    except Exception as error:
        print(error)

