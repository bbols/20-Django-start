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
    pass

class Door(BaseModel):
    title = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    date_post = models.DateField()


# Create your models here.
