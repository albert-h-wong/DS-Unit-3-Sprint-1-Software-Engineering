#!/usr/bin/env python
"""
Python module for Acme Corporation Product Inventory Reports
"""

import random
from random import randint, choice, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products():
    """ Generate list of products """
    # After cleaning up linter suggestions, all the code was moved
    # down to inventory report and results worked but not enough
    # time to figure out how to make it work with generate products
    # class


def inventory_report(self):
    """ Inventory Report """

    # Create two list of 30 random adjectives and nouns
    adjresults = []
    for _ in range(30):
        adj_selection = random.choice(ADJECTIVES)
        adjresults.append(adj_selection)

    nounresults = []
    for _ in range(30):
        noun_selection = random.choice(NOUNS)
        nounresults.append(noun_selection)

    # Zip together the results
    key = adjresults
    values = nounresults
    zip(key, values)

    # Create a list the paired adjectives and nouns
    prodnames = list(zip(key, values))

    nameslist = [x for t in prodnames for x in t]

    # Combine the list of names with a space in between
    combinednamelist = [" ".join(nameslist[0:2]), " ".join(nameslist[2:4]),
                        " ".join(nameslist[4:6]), " ".join(nameslist[6:8]),
                        " ".join(nameslist[8:10]), " ".join(nameslist[10:12]),
                        " ".join(nameslist[12:14]), " ".join(nameslist[14:16]),
                        " ".join(nameslist[16:18]), " ".join(nameslist[18:20]),
                        " ".join(nameslist[20:22]), " ".join(nameslist[22:24]),
                        " ".join(nameslist[24:26]), " ".join(nameslist[26:28]),
                        " ".join(nameslist[28:30]), " ".join(nameslist[30:32]),
                        " ".join(nameslist[32:34]), " ".join(nameslist[34:36]),
                        " ".join(nameslist[36:38]), " ".join(nameslist[38:40]),
                        " ".join(nameslist[40:42]), " ".join(nameslist[42:44]),
                        " ".join(nameslist[44:46]), " ".join(nameslist[46:48]),
                        " ".join(nameslist[48:50]), " ".join(nameslist[50:52]),
                        " ".join(nameslist[52:54]), " ".join(nameslist[54:56]),
                        " ".join(nameslist[56:58]), " ".join(nameslist[58:60])]

    number_of_products = len(combinednamelist)
    unique_product_names = len(set(combinednamelist))

    # Product average calculations
    prod_price = []
    for _ in range(30):
        price_range = randint(5, 100)
        prod_price.append(price_range)

    price_average = sum(prod_price) / number_of_products

    prod_weight = []
    for _ in range(30):
        weight_range = randint(5, 100)
        prod_weight.append(weight_range)

    weight_average = sum(prod_weight) / number_of_products

    prod_flammability = []
    for _ in range(30):
        flammability_range = random.uniform(0.0, 2.5)
        prod_flammability.append(flammability_range)

    flammability_average = sum(prod_flammability) / number_of_products

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique Product Names: {unique_product_names: .1f}')
    print(f'Average Price: {price_average: .1f}')
    print(f'Average Weight: {weight_average: .1f}')
    print(f'Average Flammability: {flammability_average: .1f}')


if __name__ == '__main__':
    inventory_report(generate_products())
