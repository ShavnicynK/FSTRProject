# Generated by Django 4.2.5 on 2023-09-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_image_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perevaladded',
            name='image',
        ),
    ]