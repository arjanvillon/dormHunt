# Generated by Django 3.0.1 on 2020-01-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0003_auto_20200103_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]