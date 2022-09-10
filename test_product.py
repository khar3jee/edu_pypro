"""
Unit-test for product.py
"""

import unittest

from product import Product

class ProductTestCase(unittest.TestCase):
    """Product test class"""
    def test_transform_name_for_sku(self):
        """unit-test for name in sku"""
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_transform_name_for_color(self):
        """unit-test for color in sku"""
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'BLACK'
        actual_value = small_black_shoes.transform_color_for_sku()
        self.assertEqual(expected_value, actual_value)
