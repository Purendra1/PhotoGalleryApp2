import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.urls import reverse
# Create your models here.

class Album(models.Model):
	albumid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='album_covers',blank=True,default='defaultcover.jpg')
	share = models.CharField(max_length=1,default='P',choices=(("P", "Private"),("U", "Only by URL"),("B", "Public")))

	def __str__(self):
		return f'{self.title} Album'

	def get_absolute_url(self):
		return reverse('viz-showAlbum',kwargs={'pk':self.pk})

	def save(self, *args, **kwargs):
		super().save()
		img=Image.open(self.cover.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail = (output_size)
			img.save(self.cover.path)

class Photo(models.Model):
	photoid = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4())
	description = models.TextField(blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photo_folder')
	share = models.CharField(max_length=1,default='P',choices=(("P", "Private"),("U", "Only by URL"),("B", "Public")))

	def __str__(self):
		return f'{self.photoid} Photo'

	def get_absolute_url(self):
		return reverse('viz-showPhoto',kwargs={'pk':self.pk})

	def save(self, *args, **kwargs):
		super().save()
		img=Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail = (output_size)
			img.save(self.image.path)

class UserAlbum(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	albumid = models.ForeignKey(Album,on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=1,default='M',choices=(("M", "M"),("F", "F"),("T", "T")))
    firstname = models.CharField(default='NULL',max_length=100)
    lastname = models.CharField(default='NULL',max_length=100)
    email = models.EmailField(default='noreply@user.com',blank=False)

    def __str__(self):
       	return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
    	super(Profile,self).save(*args, **kwargs)
    	img=Image.open(self.image.path)
    	if img.height > 300 or img.width > 300:
    		output_size = (300,300)
    		img.thumbnail = (output_size)
    		img.save(self.image.path)