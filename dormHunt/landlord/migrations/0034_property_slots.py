# Generated by Django 3.0.1 on 2020-01-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0033_merge_20200122_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slots',
            field=models.IntegerField(null=True),
        ),
    ]