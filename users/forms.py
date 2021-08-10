from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User, ShopUserProfile
import hashlib
import random


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
                  'last_name', 'password1', 'password2', 'age',)

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return data

    def save(self, commit=True):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha256(
            str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha256(
            (user.email + salt).encode('utf-8')).hexdigest()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-2 text-center', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-2 text-center', 'readonly': False}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-2'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-2'}))
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control py-2 custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')


class ShopUserProfileForm(forms.ModelForm):
    tagline = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Теги'
    }))
    about_me = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-2',
        'placeholder': 'О себе'
    }))

    class Meta:
        model = ShopUserProfile
        fields = ('tagline', 'about_me', 'gender')

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            if field_name == 'gender':
                field.widget.attrs['class'] = 'form-select form-control form-control'
