# Generated by Django 3.2.8 on 2022-03-27 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanWorld', '0009_alter_placeimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimages',
            name='image',
            field=models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['png'])], verbose_name='تصویر'),
        ),
    ]
