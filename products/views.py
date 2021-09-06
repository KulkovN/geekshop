from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from products.models import Product, ProductCategory


from django.conf import settings
from django.core.cache import cache
# Create your views here.

def get_links_menu():
   if settings.LOW_CACHE:
       key = 'links_menu'
       links_menu = cache.get(key)
       if links_menu is None:
           links_menu = ProductCategory.objects.filter(is_active=True)
           cache.set(key, links_menu)
       return links_menu
   else:
       return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
   if settings.LOW_CACHE:
       key = f'category_{pk}'
       category = cache.get(key)
       if category is None:
           category = get_object_or_404(ProductCategory, pk=pk)
           cache.set(key, category)
       return category
   else:
       return get_object_or_404(ProductCategory, pk=pk)


def get_products():
   if settings.LOW_CACHE:
       key = 'products'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(is_active=True, \
                         category__is_active=True).select_related('category')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(is_active=True, \
                         category__is_active=True).select_related('category')



def get_product(pk):
   if settings.LOW_CACHE:
       key = f'product_{pk}'
       product = cache.get(key)
       if product is None:
           product = get_object_or_404(Product, pk=pk)
           cache.set(key, product)
       return product
   else:
       return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
   if settings.LOW_CACHE:
       key = 'products_orederd_by_price'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(is_active=True, \
                                  category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(is_active=True,\
                                 category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
   if settings.LOW_CACHE:
       key = f'products_in_category_orederd_by_price_{pk}'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(category__pk=pk, is_active=True,\
                              category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(category__pk=pk, is_active=True, \
                              category__is_active=True).order_by('price')

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
        category_id=category_id).select_related('category') if category_id else Product.objects.all().select_related('category')

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
