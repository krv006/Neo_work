from django.test import TestCase

from apps.models import Category
from apps.serializers import CategoryModelSerializer


class TestCategorySerializer(TestCase):
    def setUp(self):
        Category.objects.create(name="text")
        Category.objects.create(name="Uy-joy")

    def test_serializer(self):
        obj = Category.objects.get(name='text')
        data = CategoryModelSerializer(obj).data
        assert isinstance(data, dict)
        assert data['id'] == obj.id
        assert data['name'] == 'text'

    def test_de_serializer(self):
        data = {"name": "text"}
        obj = CategoryModelSerializer(data=data)
        assert obj.is_valid()
        assert obj.validated_data['name'] == 'text'
