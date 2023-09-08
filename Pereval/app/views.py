import django_filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *


class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['customuser_id__email']

    def update(self, request, *args, **kwargs):
        try:
            instance = PerevalAdded.objects.get(pk=kwargs.get('pk'))
        except:
            return Response({"error": "Object does not exists!"}, status=status.HTTP_400_BAD_REQUEST)

        if instance.status != 'N':
            return Response({"state": 0, "message": "The information is under review, the change is not available!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PerevalAddedSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": 1, "message": "Information changed successfully!"}, status=status.HTTP_200_OK)

        return Response({"state": 0, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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
    serializer_class = ImageSerializer

