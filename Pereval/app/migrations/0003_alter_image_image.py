# Generated by Django 4.2.5 on 2023-09-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_perevaladded_perevalimage_perevaladded_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='image/%Y/%m/%d'),
        ),
    ]