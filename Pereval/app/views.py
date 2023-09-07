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
        pk = kwargs.get('pk', None)
        instance = self.get_object()
        instanceuser = CustomUser.objects.filter(pk=instance.customuser_id)[0]
        if instance.customuser.email != instanceuser.email \
                or instance.customuser.name != instanceuser.name \
                or instance.customuser.fam != instanceuser.fam \
                or instance.customuser.otch != instanceuser.otch \
                or instance.customuser.phone != instanceuser.phone:
            return Response({"state": 0, "message": "User data cannot be changed!"}, status=status.HTTP_400_BAD_REQUEST)
        if instance.status != 'N':
            return Response({"state": 0, "message": "The information is under review, the change is not available!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PerevalAddedSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"state": 1, "message": "Information changed successfully!"}, status=status.HTTP_200_OK)


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

