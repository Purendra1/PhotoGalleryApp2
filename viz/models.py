from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Owner(User):
	gender = models.CharField(max_length=1)
	profilepic = models.ImageField(upload_to='')
	#username = models.CharField(max_length=100,primary_key=True)
	#first_name = models.CharField(max_length=100)
	#last_name = models.CharField(max_length=100)
	#email = models.CharField(max_length=100)
	#password = models.CharField(max_length=512)

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
