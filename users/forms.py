from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User
import hashlib as hs
import random as rn


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                      'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                          'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('usersname', 'password')


class UsersRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                      'placeholder': 'Имя пользователя'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                       'placeholder': 'Адрес электронной почты'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                      'placeholder': 'Имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                      'placeholder': 'Фамилия'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                          'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                          'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def save(self):
        user = super(UsersRegisterForm, self).save()
        user.is_active = False
        salt = hs.sha256(
            str(rn.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hs.sha256(
            (user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
