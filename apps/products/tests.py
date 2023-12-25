from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from apps.products.models import Product  # Import your Product model
from apps.products.serializers import ProductSerializer
from apps.stores.models import Store

class ProductViewSetTests(APITestCase):
    def setUp(self):
        self.manager = User.objects.create(username='manager', password='managerpass', is_manager=True)
        self.store_manager = User.objects.create_user(username='store_manager', password='storemanagerpass', is_manager=False)
        self.store = Store.object.create(name="test",address="test",manager=self.manager)
        self.product_data = {
            'store': 1,  # Replace with the store ID you want to associate
            'category': 1,  # Replace with the category ID you want to associate
            'name': 'Test Product',
            'description': 'Test Description',
            'measure': 'kg',
            'price': 100,
            'barcode': '1234567890',
            'barcode_type': 'UPC',
        }
        self.client.force_authenticate(user=self.manager)

    def test_list_products(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        product = Product.objects.create(**self.product_data)
        response = self.client.get(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        response = self.client.post('/api/v1/products/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        product = Product.objects.create(**self.product_data)
        updated_data = {
            'name': 'Updated Test Product',
            'description': 'Updated Test Description',
            'measure': 'litr',
            'price': 150,
        }
        response = self.client.put(f'/api/v1/products/{product.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_product(self):
        product = Product.objects.create(**self.product_data)
        partial_updated_data = {'price': 200}
        response = self.client.patch(f'/api/v1/products/{product.id}/', partial_updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_product(self):
        product = Product.objects.create(**self.product_data)
        response = self.client.delete(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
