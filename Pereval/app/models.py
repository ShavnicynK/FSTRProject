from django.db import models
from django.core.validators import RegexValidator


phone_valid = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")


class CustomUser(models.Model):
    email = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=50, blank=True)
    fam = models.CharField(max_length=50, blank=True)
    otch = models.CharField(max_length=50, blank=True)
    phone = models.CharField(validators=[phone_valid], max_length=12, blank=True)

    def __str__(self):
        return f'{self.email} {self.fam} {self.fam} {self.otch} {self.phone}'


class Coordinates(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Level(models.Model):
    winter = models.CharField(max_length=3, blank=True)
    summer = models.CharField(max_length=3, blank=True)
    autumn = models.CharField(max_length=3, blank=True)
    spring = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Image(models.Model):
    data = models.ImageField(upload_to='image/%Y/%m/%d')
    title = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.title} {self.data}'


class PerevalAdded(models.Model):
    new = 'N'
    pending = 'P'
    accepted = 'A'
    rejected = 'R'

    STATUSES = [
        (new, 'новый'),
        (pending, 'в работе'),
        (accepted, 'принято'),
        (rejected, 'отклонено')
    ]

    beautyTitle = models.CharField(max_length=250, blank=False)
    title = models.CharField(max_length=250, blank=False)
    other_titles = models.CharField(max_length=250, blank=False)
    connect = models.CharField(max_length=250, blank=False)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=new)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ManyToManyField(Image, through='PerevalImage')


class PerevalImage(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pereval} {self.image}'

