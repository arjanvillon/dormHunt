# Generated by Django 3.0.1 on 2020-01-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0011_auto_20200121_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageroom',
            name='name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
