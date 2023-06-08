# Generated by Django 3.2.8 on 2022-03-27 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanWorld', '0005_auto_20220327_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeimages',
            name='report',
        ),
        migrations.AddField(
            model_name='reports',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cleanWorld.placeimages', verbose_name='تصاویر'),
        ),
    ]