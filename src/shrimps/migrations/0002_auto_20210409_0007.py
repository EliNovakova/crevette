# Generated by Django 3.1.7 on 2021-04-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrimps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shrimp',
            name='is_farmed',
            field=models.BooleanField(default=True),
        ),
    ]
