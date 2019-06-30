# Generated by Django 2.2.2 on 2019-06-30 04:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0011_auto_20190630_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('cff7ece9-c82a-4ddd-b107-27a91bd458fd'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('5e36cb32-0c1f-4f75-8be8-c2a6af85137c'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='noreply@user.com', max_length=254),
        ),
    ]
