from django.urls import path

from apps.views import ProductListCreateAPIView, CategoryListCreateAPIView, UserListApiView

urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user_list'),
    path('category/', CategoryListCreateAPIView.as_view(), name='category_list'),
    path('product/', ProductListCreateAPIView.as_view(), name='product_list'),
]
