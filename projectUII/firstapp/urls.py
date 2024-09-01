from .views import index_view,form_view

from django.urls import path

urlpatterns = [
    path('index/', index_view,name='index'),
    path('form/',form_view,name='form')
]