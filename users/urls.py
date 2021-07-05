from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path ('logout/', logout, name='logout' ),
    path('verify/<email>/<key>', verify, name='verify'),
]


# path('login/', Login.as_view(), name='login'),
# path('register/', Register.as_view(), name='register'),
# path('profile/<int:pk>/', profile, name='profile'),