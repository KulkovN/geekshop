from django.urls import path

from products.views import products, show_contacts

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('show_contacts/', show_contacts, name='show_contacts'),
    path('<int:category_id>/', products, name='product'),
    path('page/<int:page>/',  products, name='page')
]
