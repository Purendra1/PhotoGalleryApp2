# Generated by Django 2.2.2 on 2019-06-30 04:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0010_auto_20190629_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('5ee61c06-cc87-4044-96cc-5cbc0a949ba5'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, default='defaultcover.jpg', upload_to='album_covers'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('d8c733d1-ccac-413c-a69c-530bdc00a4a9'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='noreply@user.com', max_length=254, unique=True),
        ),
    ]
