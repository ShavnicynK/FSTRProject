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

    class Meta:
        model = Image
        fields = ('title', 'image')


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
            'image'
        )

    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser_email = customuser_data['email']
        customuser_fam = customuser_data['fam']
        customuser_name = customuser_data['name']
        customuser_otch = customuser_data['otch']
        customuser_phone = customuser_data['phone']
        if CustomUser.object.filter(email=customuser_email).exist():
            customuser_id = CustomUser.object.filter(email=customuser_email)[0]
        else:
            CustomUser.objects.create(
                email=customuser_email,
                fam=customuser_fam,
                name=customuser_name,
                otch=customuser_otch,
                phone=customuser_phone
            )
            customuser_id = CustomUser.object.filter(email=customuser_email)[0]

        coordinates_data = validated_data.pop('coordinates')
        coordinates_latitude = coordinates_data['latitude']
        coordinates_longitude = coordinates_data['longitude']
        coordinates_height = coordinates_data['height']
        Coordinates.objects.create(
            latitude=coordinates_latitude,
            longitude=coordinates_longitude,
            height=coordinates_height
        )
        coordinates_id = Coordinates.object.filter(
            latitude=coordinates_latitude,
            longitude=coordinates_longitude,
            height=coordinates_height
        )[0]

        level_data = validated_data.pop('level')
        level_winter = level_data['winter']
        level_summer = level_data['summer']
        level_autumn = level_data['autumn']
        level_spring = level_data['spting']
        Level.objects.create(
            winter=level_winter,
            summer=level_summer,
            autumn=level_autumn,
            spring=level_spring
        )
        level_id = Level.object.filter(
            winter=level_winter,
            summer=level_summer,
            autumn=level_autumn,
            spring=level_spring
        )[0]

        validated_data.setdefault('customuser', customuser_id)
        validated_data.setdefault('coordinates', coordinates_id)
        validated_data.setdefault('level', level_id)
        cur_pereval = PerevalAdded.objects.create(**validated_data)

        image_data = validated_data.pop('image')
        for image in image_data:
            cur_image, status = Image.objects.get_or_create(**image)
            PerevalImage.objects.create(image=cur_image, pereval=cur_pereval)

        return cur_pereval



