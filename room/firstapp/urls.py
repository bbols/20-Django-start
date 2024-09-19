#from .views import index_view,form_view
from .views import IndexView,FormViewCBV,RoomView
from django.urls import path

from rest_framework import routers
from .api_views import RoomViewSet,CustomUserViewSet,DoorViewSet,WindowViewSet,FurnitureViewSet
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'doors', DoorViewSet)
router.register(r'wondows', WindowViewSet)
router.register(r'furnitures', FurnitureViewSet)


urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('form/',FormViewCBV.as_view(),name='form'),
    path('room/',RoomView.as_view(),name='room'),
    path('api/', include(router.urls)),
]