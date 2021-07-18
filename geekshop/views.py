from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from baskets.models import Basket
from products.models import Product, ProductCategory


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'hello',
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop - каталог',
        'categories': ProductCategory.objects.all()
    }
    products = Product.objects.filter(
        category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)


