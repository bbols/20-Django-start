from django.urls import path
from django.contrib import admin

from .views import UserLoginView,UserCreateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',UserCreateView.as_view(), name='register'),
]