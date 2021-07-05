from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
import datetime as dt

# Create your models here.



class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_image', blank=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + dt.timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True