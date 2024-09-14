from django.db import models

from custom_auth.models import CustomUser

class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Room(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def fiew_title(self):
        return "hello my name is sergey"

class Door(BaseModel):
    title = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    date_post = models.DateField()

    def fiew_date(self):
        return self.date_post

class Window(BaseModel):
    title = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    date_post = models.DateField()

    def __str__(self):
        return self.title


# Create your models here.
