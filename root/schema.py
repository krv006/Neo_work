import graphene
from graphene_django import DjangoObjectType
from apps.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'discount_price', 'short_description', 'long_description',
                  'stock', 'category', 'tags', 'is_available', 'image')


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
