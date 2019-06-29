# Generated by Django 2.2.2 on 2019-06-29 06:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0009_auto_20190629_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('e0744ab0-e705-4d36-9d8d-9cf0faf87e0e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('c7925d8a-6065-43fb-8f25-21b09817ee01'), primary_key=True, serialize=False, unique=True),
        ),
    ]
