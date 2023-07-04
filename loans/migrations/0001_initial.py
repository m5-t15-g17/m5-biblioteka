# Generated by Django 4.0.7 on 2023-07-04 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(default=None)),
                ('loan_date', models.DateField(auto_now_add=True)),
                ('expected_return', models.DateField(default=datetime.datetime(2023, 7, 11, 14, 45, 2, 501605))),
            ],
        ),
    ]