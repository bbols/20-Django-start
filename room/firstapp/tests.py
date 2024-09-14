from django.test import TestCase
from .models import Door,Room,Window
from custom_auth.models import CustomUser
from django.utils import timezone
from faker import Faker
from mixer.backend.django import mixer
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        self.date = timezone.now()
        self.user=CustomUser.objects.create_user(username='test', password='test123456')
        self.room = Room.objects.create(name='my_room',user=self.user)
        self.door = Door.objects.create(title="door_big",room=self.room,date_post=self.date)
        self.window = Window.objects.create(title="windows_big", room=self.room, date_post=self.date)

    def test_user(self):
        self.assertEqual(self.user.username,'test')
    def test_room(self):
        self.assertEqual(self.room.fiew_title(),"hello my name is sergey")
    def test_door(self):
        self.assertEqual(self.door.fiew_date(),self.date)
    def test_window(self):
        self.assertEqual(str(self.window),"windows_big")

class PostTestCaseFaker(TestCase):
    def setUp(self):
        faker = Faker()
        self.date = timezone.now()
        self.user=CustomUser.objects.create_user(username=faker.name(), password='test123456')
        self.room = Room.objects.create(name=faker.name(),user=self.user)
        self.door = Door.objects.create(title=faker.name(),room=self.room,date_post=self.date)
        self.window = Window.objects.create(title=faker.name(), room=self.room, date_post=self.date)
        print(self.user.username)
    def test_room(self):
        self.assertEqual(self.room.fiew_title(),"hello my name is sergey")
    def test_door(self):
        self.assertEqual(self.door.fiew_date(),self.date)

class PostTestCaseMixer(TestCase):
    def setUp(self):
        faker = Faker()
        self.user=mixer.blend(CustomUser)
        self.room = mixer.blend(Room)
        self.door = mixer.blend(Door)
        self.window = mixer.blend(Window)
        print('mixer',self.user.username)
        print('mixer', self.window.date_post)
        self.room_two=mixer.blend(Room,user__name='papa')
        print("mixer_short",self.room_two.name)
    def test_room(self):
        self.assertEqual(self.room.fiew_title(),"hello my name is sergey")

