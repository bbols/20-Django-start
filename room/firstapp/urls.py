#from .views import index_view,form_view
from .views import IndexView,FormViewCBV,RoomView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('form/',FormViewCBV.as_view(),name='form'),
    path('room/',RoomView.as_view(),name='room')
]