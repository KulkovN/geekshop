from django.test import TestCase
from django.test.client import Client
# Create your tests here.

from products.models import ProductCategory, Product

class TestProductsSmoke(TestCase):
    status_code_success = 200

    def setUp(self):
        cat_1 = ProductCategory.objects.create(
            name='cat 1'
        )
        Product.objects.create(
            category=cat_1,
            name='cat_1'
        )
        self.client = Client()

    def test_products_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.status_code_success)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)