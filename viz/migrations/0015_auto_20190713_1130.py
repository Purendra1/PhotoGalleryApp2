# Generated by Django 2.2.2 on 2019-07-13 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0014_auto_20190713_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumid',
            field=models.UUIDField(default=uuid.UUID('71698665-e86e-4469-887e-b1463df73778'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='share',
            field=models.CharField(choices=[('Private', 'P'), ('Only by URL', 'U'), ('Public', 'B')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoid',
            field=models.UUIDField(default=uuid.UUID('c372538f-9732-4de0-80a0-6fc356ba80d4'), primary_key=True, serialize=False, unique=True),
        ),
    ]
