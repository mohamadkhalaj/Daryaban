# Generated by Django 3.2.8 on 2022-03-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanWorld', '0003_alter_visitor_responsetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='responseTime',
            field=models.FloatField(default=None, verbose_name='زمان پاسخ (ثانیه)'),
        ),
    ]
