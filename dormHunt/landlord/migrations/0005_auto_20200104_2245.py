# Generated by Django 3.0.1 on 2020-01-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0004_auto_20200103_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='barangay',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='zip_code',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
