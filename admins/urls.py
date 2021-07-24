from django.db.models import fields
from django.urls import path

from admins.views import *


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/index/', AdminProductRead.as_view(), name='admin_products_read'),
    path('products/create/',AdminProductCreate.as_view(), name='product_create'),
]
