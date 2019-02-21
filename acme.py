#!/usr/bin/env python
"""
Python module for Acme Corporation Products
"""

from random import randint, uniform, sample


class Product:
    """Class of Acme Product
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal_score = self.price / self.weight
        if steal_score < 0.5:
            return print('Not so stealable...')
        elif 1 > steal_score >= 0.5:
            return print('Kinda stealable.')
        else:
            return print('Very stealable!')

    def explode(self):
        explode_score = self.flammability * self.weight
        if explode_score < 10:
            return print('...fizzle.')
        elif 50 > explode_score >= 10:
            return print('...boom!')
        else:
            return print('...BABOOM!!')


class BoxingGlove(Product):
    """Subclass product - BoxingGlove
    """
    def __init__(self, name=None, price=10, weight=10,
                 flammability=0.5, identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return print('That tickles')
        elif 15 > self.weight >= 5:
            return print('Hey that hurt!')
        else:
            return print('OUCH!')
