# Generated by Django 3.0.1 on 2020-03-08 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0016_expenses_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtenant',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]
