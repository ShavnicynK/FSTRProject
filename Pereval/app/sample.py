valid_test_data = {
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

test_data_without_user = {
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

test_data_without_coordinates = {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
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

test_data_without_level = {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "coordinates": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
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

test_data_without_image = {
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
            }
        }

invalid_user_test_data = {
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
                "fam": "Пупкин2",
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

invalid_coordinates_test_data = {
            "beautyTitle": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "coordinates": {
                "latitude": "asd",
                "longitude": "fe",
                "height": "sdf"
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

invalid_level_test_data = {
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
                "winter": "sdfds",
                "summer": "sdf",
                "autumn": "",
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

