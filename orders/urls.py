from django.urls import path
from orders.views import show_orders


app_name = 'orders'


urlpatterns = [
    path('check_all_orders/' , show_orders, name='check_all_orders'),
]