# Generated by Django 3.1.7 on 2021-04-09 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrimps', '0005_auto_20210409_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shrimp',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 11, 36, 1, 720251)),
        ),
    ]
