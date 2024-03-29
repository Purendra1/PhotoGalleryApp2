# Generated by Django 2.2.2 on 2019-06-28 05:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0004_auto_20190627_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.IntegerField(default=uuid.UUID('247efcc9-963a-45da-ac17-fa506ae11211'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='album_covers'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.IntegerField(default=uuid.UUID('669c8b32-cbf9-499b-9a46-3d7aa10b5680'), primary_key=True, serialize=False, unique=True),
        ),
    ]
