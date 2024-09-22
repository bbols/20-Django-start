from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Room,Door,Window,Furniture
from custom_auth.models import CustomUser
from .serializers import RoomSerializer,CustomUserSerializer,DoorSerializer,WindowSerializer,FurnitureSerializer
from rest_framework import routers, serializers, viewsets,permissions
from .models import Door,Window,Furniture
from .permissions import ReadOnly
from rest_framework.authtoken.models import Token

from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication
# ViewSets define the view behavior.
class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.prefetch_related('doors','windows','furniture').all()
    serializer_class = RoomSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DoorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated|ReadOnly]
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

class WindowViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication,BasicAuthentication ]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

class FurnitureViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

def update_token(request):
    user = request.user
    if user.auth_token:
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('profile',kwargs={'pk':user.pk}))