# Generated by Django 4.1.3 on 2022-11-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_monuments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monuments',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
