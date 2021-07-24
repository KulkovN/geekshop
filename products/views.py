from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductCategory

# Create your views here.


def index(request):
    """ index controller """
    context = {
        'title': 'GeekShop - Магазин'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    """ products controller """

    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all()}
    products_list = Product.objects.filter(
        category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products_list, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products_list'] = products_paginator
    return render(request, 'products/products.html', context)


def show_contacts(request):
    context = {
        'title': 'GeekShop - контакты',
    }
    return render(request, 'products/contacts.html', context)
