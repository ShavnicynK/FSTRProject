from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from .serializers import *
from .sample import *
from random import randint


class BaseTestCase(APITestCase):

    def setUp(self):
        self.pereval_test = PerevalAdded.objects.create(
            beautyTitle='Beauty title test',
            title='Title test',
            other_titles='Other titles test',
            connect='Connect test',
            status='N',
            customuser=CustomUser.objects.create(
                email='qwerty@mail.ru',
                fam='Пупкин',
                name='Василий',
                otch='Иванович',
                phone='+99999999999'
            ),
            coordinates=Coordinates.objects.create(
                latitude=10,
                longitude=20,
                height=30
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1B',
                autumn='1C',
                spring='1D'
            )
        )

        for i in range(1, randint(2, 5)):
            title = f'Title test {i}'
            data = f'https://images.com/image_test_{i}.jpg'
            image = Image.objects.create(title=title, data=data)
            PerevalImage.objects.create(image=image, pereval=self.pereval_test)

        self.pereval_test_second = PerevalAdded.objects.create(
            beautyTitle='Beauty title test second',
            title='Title test ',
            other_titles='Other titles test second',
            connect='Connect test second',
            status='A',
            customuser=CustomUser.objects.create(
                email='testsecond@mail.ru',
                fam='Фамилия_тест_второй',
                name='Имя_тест_второй',
                otch='Отчество_тест_второй',
                phone='+11111111111'
            ),
            coordinates=Coordinates.objects.create(
                latitude=10,
                longitude=20,
                height=30
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1B',
                autumn='1C',
                spring='1D'
            )
        )

        for i in range(1, randint(2, 5)):
            title = f'Title test second {i}'
            data = f'https://images.com/image_test_second_{i}.jpg'
            image = Image.objects.create(title=title, data=data)
            PerevalImage.objects.create(image=image, pereval=self.pereval_test_second)


class GetAllPerevalDataTest(BaseTestCase):

    def setUp(self):
        super().setUp()

    def test_get_all_pereval_data(self):
        response = self.client.get('/submitData/')
        perevals = PerevalAdded.objects.all()
        serializer = PerevalAddedSerializer(perevals, many=True)
        self.assertEqual(response.data['count'], len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetItemPerevalDataTest(BaseTestCase):

    def setUp(self):
        super().setUp()

    def test_get_item_pereval_data(self):
        url = f'/submitData/{self.pereval_test.pk}/'
        response = self.client.get(url)
        pereval = PerevalAdded.objects.get(pk=self.pereval_test.pk)
        serializer = PerevalAddedSerializer(pereval)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_not_item_pereval_data(self):
        response = self.client.get('/submitData/150/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreatePerevalDataTest(APITestCase):

    def setUp(self):
        super().setUp()

    def test_create_pereval_with_valid_data(self):
        response = self.client.post('/submitData/', valid_test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_pereval_without_user(self):
        response = self.client.post('/submitData/', test_data_without_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_pereval_without_level(self):
        response = self.client.post('/submitData/', test_data_without_level, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_pereval_without_coordinates(self):
        response = self.client.post('/submitData/', test_data_without_coordinates, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_pereval_without_image(self):
        response = self.client.post('/submitData/', test_data_without_image, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdatePerevalDataTest(BaseTestCase):

    def setUp(self):
        super().setUp()

    def test_update_pereval_with_valid_data(self):
        url = f'/submitData/{self.pereval_test.pk}/'
        response = self.client.patch(url, valid_test_data, format='json')
        self.assertEqual(response.data, {'state': 1, 'message': 'Information changed successfully!'})

    def test_update_pereval_with_invalid_coordinates(self):
        url = f'/submitData/{self.pereval_test.pk}/'
        response = self.client.patch(url, invalid_coordinates_test_data, format='json')
        pereval = PerevalAdded.objects.get(pk=self.pereval_test.pk)
        serializer = PerevalAddedSerializer(instance=pereval, data=invalid_coordinates_test_data, partial=True)
        serializer.is_valid()
        self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})

    def test_update_pereval_with_invalid_level(self):
        url = f'/submitData/{self.pereval_test.pk}/'
        response = self.client.patch(url, invalid_level_test_data, format='json')
        pereval = PerevalAdded.objects.get(pk=self.pereval_test.pk)
        serializer = PerevalAddedSerializer(instance=pereval, data=invalid_level_test_data, partial=True)
        serializer.is_valid()
        self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})

    def test_update_pereval_with_invalid_user(self):
        url = f'/submitData/{self.pereval_test.pk}/'
        response = self.client.patch(url, invalid_user_test_data, format='json')
        self.assertEqual(response.data, {'state': 0, 'message': "User data cannot be changed!"})

    def test_update_pereval_without_new_status(self):
        url = f'/submitData/{self.pereval_test_second.pk}/'
        response = self.client.patch(url, valid_test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetAllPerevalDataByEmailTest(BaseTestCase):
    def setUp(self):
        super().setUp()

    def test_get_data_by_email(self):
        response = self.client.get('/submitData/', {'customuser_id__email': 'test@mail.ru'})
        self.assertEqual(len(response.data), 4)