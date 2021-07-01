from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    # path('profile/', profile, name='profile'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path ('logout/', logout, name='logout' ),
]
