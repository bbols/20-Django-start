#from .views import index_view,form_view
from .views import IndexView,FormViewCBV,RoomView,UserDetailView
from django.urls import path

from rest_framework import routers
from .api_views import RoomViewSet,CustomUserViewSet,DoorViewSet,WindowViewSet,FurnitureViewSet,update_token
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'doors', DoorViewSet)
router.register(r'windows', WindowViewSet)
router.register(r'furniture', FurnitureViewSet)


urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('form/',FormViewCBV.as_view(),name='form'),
    path('room/',RoomView.as_view(),name='room'),
    path('profile/<int:pk>/',UserDetailView.as_view(),name='profile'),
    path('updatetoken/',update_token,name='update_token'),
    path('api/v0/', include(router.urls)),
]