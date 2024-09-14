from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    def view_take(self):
        return "custom_auth"