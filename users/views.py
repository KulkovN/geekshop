from django.urls.base import reverse_lazy
from users.models import User
# from django import forms
# import django
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from common.views import CommonContextMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


from users.forms import UserLoginForm, UsersRegisterForm, UserProfileForm
from baskets.models import Basket


class Login(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Авторизация'
        return context


class Register(CreateView):
    """ class - register_new_user-template """
    model = User
    template_name = 'users/register.html'
    form_class = UsersRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Регистрация'
        return context


# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(
#             data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=user)
#     context = {
#         'title': 'GeekShop - Личный кабинет',
#         'form': form,
#         'baskets': Basket.objects.filter(user=user),
#     }
#     return render(request, 'users/profile.html', context)

class Profile(CommonContextMixin, UpdateView):
   
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'GeekShop - Личный кабинет'
    # success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.pk))

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
