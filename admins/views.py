from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


# Create your views here.
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from products.models import Product, ProductAdminForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {'title': 'Админка Geekshop | Пользователи'}
    return render(request, 'admins/admin.html', context)


# CRUD
class UserListView(ListView):
    """ class - rendering main-template """
    model = User
    template_name = 'admins/admin_users_read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка Geekshop | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    """ class - rendering create_user-template """
    model = User
    template_name = 'admins/admin_users_create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка Geekshop | Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    """ class - rendering update_user-template """
    model = User
    template_name = 'admins/admin_users_update_delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка | Обновление пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    """ class - rendering delete_user-template """
    model = User
    template_name = 'admins/admin_users_update_delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminProductRead(ListView):
    """ class - rendering main-admin_product-template """
    model = Product
    template_name = 'admins/admin_products_read.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(AdminProductRead, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop | Продукты'
        return context


class AdminProductCreate(CreateView):
    """ class - rendering main-admin_product-create-template """
    model = Product
    template_name = 'admins/product_create.html'
    success_url = reverse_lazy('admins:admin_products_read')
    fields = ('name', 'image', 'description', 'price', 'quantity', 'category',)

    def get_context_data(self, **kwargs):
        context = super(AdminProductCreate, self).get_context_data(**kwargs)
        context['title'] = 'Админка Geekshop | Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCreate, self).dispatch(request, *args, **kwargs)
