# Generated by Django 3.0.7 on 2020-10-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtpixel', '0008_auto_20201002_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]