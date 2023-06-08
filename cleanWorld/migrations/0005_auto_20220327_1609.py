# Generated by Django 3.2.8 on 2022-03-27 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanWorld', '0004_alter_visitor_responsetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitor',
            options={'verbose_name': 'بازدید کننده', 'verbose_name_plural': 'بازدید کنندگان'},
        ),
        migrations.CreateModel(
            name='placeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cleanWorld.reports', verbose_name='تصاویر')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]