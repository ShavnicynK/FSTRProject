from .models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'fam', 'name', 'otc', 'phone')


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'height')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('title', 'image')
