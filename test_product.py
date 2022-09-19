"""
Unit-test for product.py
"""

from product import Product

class TestCase():
    """Product test class"""
    def test_transform_name_for_sku(self):
        """unit-test for name in sku"""
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.transform_name_for_sku() == 'SHOES'

    def test_transform_name_for_color(self):
        """unit-test for color in sku"""
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.transform_color_for_sku() == 'BLACK'

    def test_generate_sku(self):
        """unit-test for generate_sku"""
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.generate_sku() == 'SHOES-S-BLACK'
