# Generated by Django 3.0.1 on 2020-02-24 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0008_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expenses',
            name='date_paid',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='expenses',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
    ]