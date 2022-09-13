"""
unittest mocking for tax file
https://docs.python.org/3/library/unittest.html
"""
import io
import unittest
from unittest import mock

from tax import add_sales_tax

class SalesTaxTestCase(unittest.TestCase):
    @mock.patch('tax.urlopen')
    def test_get_sales_tax_returns_proper_value_from_api(
        self,
        mock_urlopen
    ):
        test_tax_rate = 1.05
        mock_urlopen.return_value = io.BytesIO(
            str(test_tax_rate).encode('utf-8')
        )
        
        self.assertEqual(
            5 * test_tax_rate,
            add_sales_tax(5, 'USA', 'MI')
        )
