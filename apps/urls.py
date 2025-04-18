from django.urls import path

from apps.views import ProductListCreateAPIView, CategoryListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='product_list'),
    path('product/', ProductListCreateAPIView.as_view(), name='product_list'),
]
