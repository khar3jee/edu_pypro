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

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('Pants', 'L', 'blue')
        cart.add_product(product)
        
        self.assertDictEqual({'PANTS-L-BLUE': {'quantity': 1}}, cart.products)

    def test_remove_product(self):
        cart = ShoppingCart()
        product = Product('Pants', 'L', 'blue')
        cart.add_product(product)
        cart.remove_product(product)
        
        self.assertDictEqual({}, cart.products)
    
    def test_add_different_products(self):
        cart = ShoppingCart()
        product_a = Product('shoes', 'S', 'red')
        cart.add_product(product_a)

        product_b = Product('Pants', 'L', 'blue')
        cart.add_product(product_b)
        #print(cart.products)
        self.assertDictEqual(
            {
            'PANTS-L-BLUE': {'quantity': 1},
            'SHOES-S-RED': {'quantity': 1}
            },
            cart.products)
    
    def test_remove_too_many_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'red')
        cart.add_product(product)
        cart.remove_product(product, quantity=2)

        self.assertDictEqual({}, cart.products)
