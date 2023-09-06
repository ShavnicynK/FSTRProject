from django.db import models
from django.core.validators import RegexValidator


phone_valid = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")


class CustomUser(models.Model):
    email = models.CharField(max_length=200, unique=True, blank=False)
    name = models.CharField(max_length=50, blank=True)
    fam = models.CharField(max_length=50, blank=True)
    otch = models.CharField(max_length=50, blank=True)
    phone = models.CharField(validators=[phone_valid], max_length=12, blank=True)

    def __str__(self):
        return f'{self.email} {self.fam} {self.fam} {self.otch} {self.phone}'
