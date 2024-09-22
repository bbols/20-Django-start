from django.urls import path, include
from .models import Room,Door,Window,Furniture
from rest_framework import routers, serializers, viewsets

from custom_auth.models import CustomUser


# Serializers define the API representation.
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    doors = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='door-detail',
        read_only = True
    )
    windows = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='window-detail',
        read_only=True
    )
    furniture = serializers.HyperlinkedRelatedField(
        many=True,
        view_name = 'furniture-detail',
        read_only=True
    )
    class Meta:
        model = Room
        fields = ['user','doors','windows','furniture']

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        lookup_field = 'id'

class DoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'

class WindowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Window
        fields = '__all__'

class FurnitureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
