# Generated by Django 3.0.1 on 2020-02-05 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='move_in_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='application',
            name='schedule',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
