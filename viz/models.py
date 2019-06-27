from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
	albumid = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=100)
	description = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='')

class Photo(models.Model):
	photoid = models.IntegerField(primary_key=True)
	description = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='')

class UserAlbum(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=1,default='M')

    def __str__(self):
        return f'{self.user.username} Profile'