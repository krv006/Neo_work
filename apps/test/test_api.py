from django.test import TestCase, Client
from django.urls import reverse
from apps.models import Category

class TestCategoryAPI(TestCase):
    def setUp(self):
        Category.objects.create(name='Uy-joy')
        Category.objects.create(name='Texnika')
        self.client = Client()
        self.url = reverse('category_list')

    def test_category_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
