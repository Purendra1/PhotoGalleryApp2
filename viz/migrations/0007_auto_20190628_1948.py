# Generated by Django 2.2.2 on 2019-06-28 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0006_auto_20190628_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('c5b1581d-a314-454d-8840-b5fa4e95bcaa'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('dbb690b0-1a8a-462d-9075-943d7d58735e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
