# Generated by Django 4.0.7 on 2023-07-04 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='expected_return',
            field=models.DateField(default=datetime.datetime(2023, 7, 11, 14, 45, 57, 280869)),
        ),
    ]