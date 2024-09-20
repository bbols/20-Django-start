from .models import Room,Door,Window,Furniture
from custom_auth.models import CustomUser
from .serializers import RoomSerializer,CustomUserSerializer,DoorSerializer,WindowSerializer,FurnitureSerializer
from rest_framework import routers, serializers, viewsets
# ViewSets define the view behavior.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

class WindowViewSet(viewsets.ModelViewSet):
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

