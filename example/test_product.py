from product import Product
import unittest


class ProductTestCase(unittest.TestCase):
    # Set up test scenario
    def setUp(self):
        self.product = Product('shoes', 'S', 'black')

    @unittest.skip('demonstrating skipping')
    def test_transform_name(self):
        expected_value = 'SHOES'
        actual_value = self.product.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    @unittest.skip('demonstrating skipping')
    def test_transform_color_for_sku(self):
        expected_value = 'BLACK'
        actual_value = self.product.transform_color_for_sku()
        self.assertEqual(expected_value, actual_value)

    @unittest.skip('demonstrating skipping') # skip decorator
    def test_generate_sku(self): 
        expected_value = 'SHOES-S-BLACK'
        actual_value = self.product.generate_sku()
        self.assertEqual(expected_value, actual_value)
    # Finish
    def tearDown(self):
        del self.product
