from products.models import Product
from django import forms
from django.forms.models import ModelForm


from users.forms import UserProfileForm, UsersRegisterForm
from users.models import User


class UserAdminRegisterForm(UsersRegisterForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name',
                  'last_name', 'password1', 'password2')
        avatar = forms.ImageField(widget=forms.FileInput(
            attrs={'class': 'custom-file-input'}), required=False)


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': False}))
