import django_filters
from rest_framework import viewsets
from .serializers import *
from .models import *


class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['customuser_id__email']


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer()

