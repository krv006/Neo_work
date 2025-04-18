from rest_framework.serializers import ModelSerializer

from apps.models import User, Category, Product


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data if instance.category else None
        return repr
