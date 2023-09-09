# REST API for FSTR Pereval.app


Представляю вашему вниманию REST API, разработанный на Django Rest Framework.

Данный REST API предназначен для обмена данными вымышленного приложения и сервера Федерации спортивного туризма России.


Легенда приложения:

Пользователь с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:

        координаты перевала и его высота;
        имя пользователя;
        почта и телефон пользователя;
        название перевала;
        несколько фотографий перевала.

Для передачи указанных данных был реализован метод, который принимает POST-запрос https://srv9.ru/submitData/, принимающий данные в JSON-формате
Пример загружаемых данных в JSON:
```json
{
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "customuser": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otch": "Иванович",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "Седловина",
                    "data": "https://images.com/image1.jpg"
                },
                {
                    "title": "Подъём",
                    "data": "https://images.com/image1.jpg"
                }
            ]
        }
```
В процессе работы была проведена оптимизаци базы данных, предоставленной ФСТР.
В результате работы было создано 5 таблиц:

- CustomUser (пользователи, добавляющие информацию)
- Coordinates (координаты перевала)
- Level (уровни сложности перевала)
- Image (фотографии перевала)
- PerevalAdded (информация о самом перевале)


## Реализованные методы
#### GET /submitData/
Возвращает все записи с перевалами

Запрос:
```html
https://srv9.ru/submitData/
```

Ответ:
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "add_time": "2023-09-09T11:41:37.381282Z",
            "status": "N",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "customuser": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otch": "Иванович",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "Седловина",
                    "data": "https://images.com/image1.jpg"
                },
                {
                    "title": "Подъём",
                    "data": "https://images.com/image1.jpg"
                }
            ]
        },
        {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "add_time": "2023-09-09T12:07:28.369197Z",
            "status": "N",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "customuser": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otch": "Иванович",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "Седловина",
                    "data": "https://images.com/image1.jpg"
                },
                {
                    "title": "Подъём",
                    "data": "https://images.com/image1.jpg"
                }
            ]
        },
        {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "add_time": "2023-09-09T12:24:04.201870Z",
            "status": "N",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "customuser": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otch": "Иванович",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "Седловина",
                    "data": "https://images.com/image1.jpg"
                },
                {
                    "title": "Подъём",
                    "data": "https://images.com/image1.jpg"
                }
            ]
        }
    ]
}
```

#### POST /submitData/
Добавляет запись о перевале

Запрос:
```html
https://srv9.ru/submitData/
```

Ответ:
```json
{
    "beautyTitle": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2023-09-09T12:24:04.201870Z",
    "status": "N",
    "coordinates": {
        "latitude": 45.3842,
        "longitude": 7.1525,
        "height": 1200
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "customuser": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otch": "Иванович",
        "phone": "+99999999999"
    },
    "image": [
        {
            "title": "Седловина",
            "data": "https://images.com/image1.jpg"
        },
        {
            "title": "Подъём",
            "data": "https://images.com/image1.jpg"
        }
    ]
}
```

#### GET /submitData/{id}
Возвращает запись по перевале с указанным ID

Запрос:
```html
https://srv9.ru/submitData/2/
```

Ответ:
```json
{
    "beautyTitle": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2023-09-09T12:07:28.369197Z",
    "status": "N",
    "coordinates": {
        "latitude": 45.3842,
        "longitude": 7.1525,
        "height": 1200
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "customuser": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otch": "Иванович",
        "phone": "+99999999999"
    },
    "image": [
        {
            "title": "Седловина",
            "data": "https://images.com/image1.jpg"
        },
        {
            "title": "Подъём",
            "data": "https://images.com/image1.jpg"
        }
    ]
}
```


#### PATCH /submitData/{id}
Вносит изменения в данные о превале с указанным ID

Запрос:
```html
https://srv9.ru/submitData/2/
```

Ответ:
```json
{
    "state": 1,
    "message": "Information changed successfully!"
}
```


#### GET /submitData/?customuser_id__email={email}
Возвращает все записи о перевалах, которые сделал пользователь с указанным EMAIL

Запрос:
```html
https://srv9.ru/submitData/?customuser_id__email=qwerty%40mail.ru
```

Ответ:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "add_time": "2023-09-09T11:41:37.381282Z",
            "status": "N",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "customuser": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otch": "Иванович",
                "phone": "+99999999999"
            },
            "image": [
                {
                    "title": "Седловина",
                    "data": "https://images.com/image1.jpg"
                },
                {
                    "title": "Подъём",
                    "data": "https://images.com/image1.jpg"
                }
            ]
        }
    ]
}
```



Протестировать методы можно с использованием документации OpenAPI и Swagger по адресам:

https://srv9.ru/swagger/

https://srv9.ru/redoc/