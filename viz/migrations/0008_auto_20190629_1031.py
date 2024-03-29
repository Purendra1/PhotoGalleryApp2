# Generated by Django 2.2.2 on 2019-06-29 05:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0007_auto_20190628_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='noreply@user.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('ee0702a4-1b40-428a-8b5f-035471871869'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('903c10d5-b35c-40d9-9e6f-6040ad0eab76'), primary_key=True, serialize=False, unique=True),
        ),
    ]
