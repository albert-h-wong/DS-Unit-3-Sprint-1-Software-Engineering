#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import inventory_report, ADJECTIVES, NOUNS
from random import randint


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_explode_set_value(self):
        """Test product explode value."""
        prod2 = Product('Test2', weight=50,
                        flammability=0.8)
        self.assertEqual(prod2.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme report are the correct"""
    def test_default_num_products(self):
        """Test default number of product report is 30."""
        report = inventory_report()
        self.assertEqual(self.report.number_of_products, 30)

    def test_legal_names(self):
        """Test product naming convention."""
        report = inventory_report()
        product_names = report.combinednamelist
        adj_list = ADJECTIVES()
        noun_list = NOUNS()
        random_prod_selection = random.choice(product_names)
        self.assertIN(adj_list, random_prod_selection)
        self.assertIN(noun_list, random_prod_selection)
        self.assertIN(" ", random_prod_selection)


if __name__ == '__main__':
    unittest.main()
