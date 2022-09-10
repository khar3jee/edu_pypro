"""
Integration-test for cart.py
"""
import unittest
from product import Product
from cart import ShoppingCart

class ShoppingCartTestCase(unittest.TestCase):
    """tests ShoppingCart"""
    def test_add_and_remove_product(self):
        """starts ShoppingCart instance, and
         Product instance then add and removes products
         to and from cart then checks with assert"""

        cart = ShoppingCart()
        product = Product('shoes', 'S', 'red')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)
