from django.db import models

from custom_auth.models import CustomUser
#Менеджер

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

#База данных
class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Room(BaseModel):
    #не обязательно указвать, он ставиться по умолчанию это для наглядности
    objects = models.Manager()
    #менеджер мой
    active_objects= ActiveManager()


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #двери
    doors=models.ManyToManyField('Door',blank=True)
    #окна
    windows=models.ManyToManyField('Window',blank=True)

    #фурнитура
    furniture=models.ManyToManyField('Furniture',blank=True)


    def __str__(self):
        return f"{self.name} | куратор {self.user}"


class Door(BaseModel):
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    date_post = models.DateField()
    def __str__(self):
        return f"{self.name} | {self.material} | {self.color}"

class Window(BaseModel):
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    date_post = models.DateField()
    def __str__(self):
        return f"{self.name} | {self.size} | {self.material}"

class Furniture(BaseModel):
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} | {self.type} | {self.color}"

    def __str__(self):
        return self.name


# Create your models here.
