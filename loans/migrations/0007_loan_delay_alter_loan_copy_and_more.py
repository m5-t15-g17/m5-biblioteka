# Generated by Django 4.0.7 on 2023-07-06 17:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0006_alter_loan_expected_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='delay',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='loan',
            name='copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loan',
            name='expected_return',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 14, 52, 33, 180674)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copies.copy'),
        ),
    ]
