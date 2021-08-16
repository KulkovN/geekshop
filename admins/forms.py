from products.models import Product, ProductCategory
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

    class Meta:
        pass


class AdminProductCategoryCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}), required=False)
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}),
                                  label='скидка', required=False, min_value=0, max_value=90, initial=0)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'discount',)


class AdminProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select form-control'}))
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')
