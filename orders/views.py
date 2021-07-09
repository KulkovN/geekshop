from django.shortcuts import render
from .models import Order

# Create your views here.

def show_orders(request):
    context = { 
        'title':'GeekShop | Заказы',
        'object_list':Order.objects.all()
    }
    return render (request, 'orders/check_orders.html', context)