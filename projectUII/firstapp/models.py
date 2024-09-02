from django.db import models

class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Room(BaseModel):
    pass

class Door(BaseModel):
    title = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_post = models.DateField()


# Create your models here.
