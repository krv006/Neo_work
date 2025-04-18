from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.models import Category, Product, User
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, UserModelSerializer


@extend_schema(tags=['User'])
class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['Product'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['Product'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
