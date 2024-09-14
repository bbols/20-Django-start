from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#сигналы
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    def view_take(self):
        return "custom_auth"

    #переопределение базового метода save
    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)
    #    # Создание профиля пользователя
    #    if not Profile.objects.filter(user=self).exists():
    #        Profile.objects.create(user=self)

class Profile(models.Model):
    info = models.TextField(blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

@receiver(post_save, sender=CustomUser)#instance это обьект post_save | sender это CustomUser
def create_user_profile(sender, instance, **kwargs):
    print("Сработал обработчик сигнала")
    if not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)