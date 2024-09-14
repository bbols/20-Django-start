#TODO тест views.py

from django.test import Client
from django.test import TestCase
from custom_auth.models import CustomUser

class OpenViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        print("start test views.py")

    def test_statuser(self):
        #TODO GET
        #проверка ответа со страницы логин
        response = self.client.get('/login/')
        print(response.status_code,'await to ',200)
        self.assertEqual(response.status_code, 200)
        # проверка ответа с дефотлтной не настроенно на текущий момент страницы
        response = self.client.get('/')
        print(response.status_code, 'await to ', 404)
        self.assertEqual(response.status_code, 404)

        #TODO POST
        response = self.client.post("/room/", {'name': '123', 'passwd': '123'})
        print('POST',response.status_code, 'await to ', 302)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        user = CustomUser.objects.create_user(username='admin', password='admin')

        # TODO login
        response = self.client.get('/room/')
        self.assertEqual(response.status_code,302)
        response = self.client.login(username='admin', password='admin')
        response = self.client.get('/room/')
        print('login', response.status_code, 'await to ', 200)
        self.assertEqual(response.status_code, 200)



