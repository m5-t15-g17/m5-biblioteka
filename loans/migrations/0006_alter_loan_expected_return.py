# Generated by Django 4.0.7 on 2023-07-04 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_alter_loan_expected_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='expected_return',
            field=models.DateField(default=datetime.datetime(2023, 7, 11, 17, 42, 19, 13144)),
        ),
    ]
