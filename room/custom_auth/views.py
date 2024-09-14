from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

from django.views.generic import CreateView
from .forms import RegistrationForm
from  .models import CustomUser

class UserLoginView(LoginView):
    template_name = 'custom_auth/login.html'

class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'custom_auth/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("login")




    