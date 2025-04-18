from django.test import TestCase

from apps.models import Category


class TestCategoryView(TestCase):
    def setUp(self):
        Category.objects.get_or_create(name="Texnika")
        Category.objects.get_or_create(name="Uy-joy")

    def testing_list(self):
        obj = Category.objects.all()
        self.assertEqual(len(obj), 2)

    def test_get(self):
        obj = Category.objects.get(name='Texnika')
        assert obj.id == obj.id
        assert obj.name == 'Texnika'
