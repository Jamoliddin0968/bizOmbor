from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from apps.products.models import Product  # Import your Product model
from apps.products.serializers import ProductSerializer
from apps.stores.models import Store
from apps.categories.models import Category
class ProductViewSetTests(APITestCase):
    def setUp(self):
        self.manager = User.objects.create(username='manager', password='managerpass', is_manager=True)
        self.store_manager = User.objects.create(username='store_manager', password='storemanagerpass', is_manager=False)
        self.store = Store.objects.create(name="test",address="test",manager=self.manager)
        self.category = Category.objects.create(name="test")
        self.manager_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjE1fQ.amdse1iXH1m-SYlFwdEjGbgigb_81RdQZpz9LPF79Zc"
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.manager_token}')
        self.product_data = {
            'store': self.store,  # Replace with the store ID you want to associate
            'category': self.category,  # Replace with the category ID you want to associate
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



    def test_partial_update_product(self):
        product = Product.objects.create(**self.product_data)
        partial_updated_data = {'price': 200}
        response = self.client.patch(f'/api/v1/products/{product.id}/', partial_updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    def test_destroy_product(self):
        product = Product.objects.create(**self.product_data)
        response = self.client.delete(f'/api/v1/products/{product.id}/')
    def test_destroy_product(self):
        product = Product.objects.create(**self.product_data)
        response = self.client.delete(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
