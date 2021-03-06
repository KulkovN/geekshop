from django.db.models.query_utils import select_related_descend
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages


# Create your views here.


from users.forms import UserLoginForm, UsersRegisterForm, UserProfileForm, ShopUserProfileForm
from baskets.models import Basket


def login(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_name = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=user_name, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UsersRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verify_mail(user)
            messages.success(
                request, ('Ваш профиль создан. В целях продуктивного использования ресурса - активируйте профиль.\n\
Для этого следуйте инструкциям из письма, направленного Вам на адрес электронный почты, указанный при регистрации.'))
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UsersRegisterForm()

    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


def send_verify_mail(user):
    # verify mesage generate
    verify_link = reverse('users:verify', args=[
                          user.email, user.activation_key])
    title = f'Подтверждение учетной записи пользователя {user.username}'
    message = f'Для подтверждения учетной записи пользователя {user.username} на GeekShop Store \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, key, backend='django.contrib.auth.backends.ModelBackend'):
    # verify function
    user = User.objects.filter(email=email).first()
    if user and user.activation_key == key and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = ''
        user.activation_key_created = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return render(request, 'users/verify.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            data=request.POST, files=request.FILES, instance=request.user)
        profile_form = ShopUserProfileForm(
            data=request.POST, instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = ShopUserProfileForm(
            instance=request.user.shopuserprofile)
    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
