from .models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'fam', 'name', 'otch', 'phone')


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'height')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.CharField()

    class Meta:
        model = Image
        fields = ('title', 'data')


class PerevalAddedSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelSerializer()
    image = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = (
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'status',
            'coordinates',
            'level',
            'customuser',
            'image',
        )

    def create(self, validated_data):
        image_data = validated_data.pop('image')

        customuser_data = validated_data.pop('customuser')
        if CustomUser.objects.filter(email=customuser_data['email']).exists():
            customuser = CustomUser.objects.get(email=customuser_data['email'])
        else:
            customuser = CustomUser.objects.create(**customuser_data)

        coordinates_data = validated_data.pop('coordinates')
        coordinates = Coordinates.objects.create(**coordinates_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        validated_data.setdefault('customuser', customuser)
        validated_data.setdefault('coordinates', coordinates)
        validated_data.setdefault('level', level)
        cur_pereval = PerevalAdded.objects.create(**validated_data)

        if len(image_data) > 0:
            for image in image_data:
                cur_image = Image.objects.create(**image)
                PerevalImage.objects.create(image=cur_image, pereval=cur_pereval)

        return cur_pereval

    def update(self, instance, validated_data):
        instance.beautyTitle = validated_data.get('beautyTitle')
        instance.btitle = validated_data.get('title')
        instance.other_titles = validated_data.get('other_titles')
        instance.connect = validated_data.get('connect')
        instance.status = validated_data.get('status')

        coordinates_data = validated_data.get('coordinates')
        Coordinates.objects.filter(pk=instance.coordinates_id).update(
            latitude=coordinates_data['latitude'],
            longitude=coordinates_data['longitude'],
            height=coordinates_data['height']
        )

        level_data = validated_data.get('level')
        Level.objects.filter(pk=instance.level_id).update(
            winter=level_data['winter'],
            summer=level_data['summer'],
            autumn=level_data['autumn'],
            spring=level_data['spring']
        )

        image_data = validated_data.get('image')
        old_image = PerevalImage.objects.filter(pereval=instance)
        if old_image:
            for image in old_image:
                image.delete()
        for image in image_data:
            cur_image = Image.objects.create(**image)
            PerevalImage.objects.create(image=cur_image, pereval=instance)

        instance.save()
        return instance



