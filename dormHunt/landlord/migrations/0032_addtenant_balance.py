# Generated by Django 3.0.1 on 2020-01-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0031_auto_20200122_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtenant',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
