# Generated by Django 3.2.12 on 2022-02-26 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0002_auto_20220226_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscription_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]