#from django.test import TestCase
from django.test import TestCase
from .models import CustomUser


# Create your tests here.


class CustomAuthTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='test', password='test12345678',email='1@1.ru')

    def test_str(self):
        print(f"start test user - {str(self.user)} - 1@1.ru")
        self.assertEqual(str(self.user), '1@1.ru')

    def test_print(self):
        print(f"start test user - {self.user.view_take()} - custom_auth")
        self.assertEqual(self.user.view_take(), "custom_auth")
