from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.reverse import reverse
from rest_framework.request import Request
from rest_framework import status
from .views import *


class TestApiPerevalAdded(APITestCase):

    def test_submitdata(self):
        data = {
            "beautyTitle": "string",
            "title": "string",
            "other_titles": "string",
            "connect": "string",
            "add_time": "2023-09-08T10:33:11.508224Z",
            "status": "N",
            "coordinates": {
                "latitude": 0.0,
                "longitude": 0.0,
                "height": -2147483648
            },
            "level": {
                "winter": "str",
                "summer": "str",
                "autumn": "str",
                "spring": "str"
            },
            "customuser": {
                "email": "string@mail.ru",
                "fam": "string",
                "name": "string",
                "otch": "string",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "string",
                    "data": "https://dba-presents.com/images/java/java/SendFileRest/image_file.png"
                },
                {
                    "title": "string2",
                    "data": "https://dba-presents.com/images/java/java/SendFileRest/csv_file.png"
                }
            ]
        }

        response = self.client.post(reverse('submitData'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getdata(self):
        response = self.client.get(reverse('submitData'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
