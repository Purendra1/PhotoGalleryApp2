import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Album(models.Model):
	albumid = models.IntegerField(primary_key=True, unique=True, default=uuid.uuid4())
	title = models.CharField(max_length=100)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='album_covers')

class Photo(models.Model):
	photoid = models.IntegerField(primary_key=True,unique=True, default=uuid.uuid4())
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='')

class UserAlbum(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=1,default='M',choices=(("M", "M"),("F", "F"),("T", "T")))

    def __str__(self):
       	return f'{self.user.username} Profile'

    def save(self):
    	super().save()
    	img=Image.open(self.image.path)
    	if img.height > 300 or img.width > 300:
    		output_size = (300,300)
    		img.thumbnail = (output_size)
    		img.save(self.image.path)