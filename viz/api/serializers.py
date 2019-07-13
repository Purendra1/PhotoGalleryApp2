from rest_framework import serializers
from viz.models import *
from rest_framework.serializers import (
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from django.contrib import messages
from rest_framework import routers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.fields import CurrentUserDefault

class AlbumListSerializer(serializers.ModelSerializer):
	detail_url = HyperlinkedIdentityField(
		view_name='viz-api-albumDetails'
		)
	class Meta:
		model=Album
		fields = [
			'detail_url',
			'title',
			'date_posted',
			'owner',
			'cover',
		]



class AlbumDetailSerializer(serializers.ModelSerializer):
	photos = SerializerMethodField()
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'date_posted',
			'owner',
			'cover',
			'photos'
		]

	def get_photos(self,obj):
		qs = Photo.objects.filter(albumid=obj)
		serializer_context = {
    	'request': self.context['request'],
		}
		photos = PhotoListSerializer(qs,many=True,context=serializer_context).data
		return photos

class AlbumUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'cover',
			'share'
		]
		
class AlbumCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'cover',
			'share'
		]

	def create(self, validated_data):
		image = validated_data.pop('cover')
		album = Album.objects.create(**validated_data)
		album.cover = image
		return album


############################################################################################################################



class PhotoCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields = [
			'description',
			'albumid',
			'image'
		]

	def get_fields(self, *args, **kwargs):
		fields = super(PhotoCreateSerializer, self).get_fields(*args, **kwargs)
		req = self.context['request']
		url = req.build_absolute_uri()
		i = url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		qs=Album.objects.filter(albumid=key)
		fields['albumid'].queryset = qs
		return fields


	def create(self, validated_data):
		return Photo.objects.create(**validated_data)

	

class PhotoListSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='viz-api-photoDetails'
		)
	class Meta:
		model=Photo
		fields = [
			'url',
			'photoid',
			'date_posted',
			'owner',
			'albumid'
		]


class PhotoDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields = [
			'photoid',
			'description',
			'date_posted',
			'owner',
			'albumid',
			'image'
		]


class PhotoUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields = [
			'description',
		]
		



############################################################################################################################



class UserCreateSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
        label = "Confirm Password"
    )
	password = serializers.CharField(
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
        label = "Password"
    )
	firstname = serializers.CharField(label = "First Name",required=False)
	lastname = serializers.CharField(label = "Last Name",required=False)
	gender = serializers.ChoiceField(label="Gender",default='M',choices=(("M", "M"),("F", "F"),("T", "T")))
	image = serializers.ImageField(label="Profile Picture",required=False)
	class Meta:
		model = User
		fields = [
		'username',
		'password',
		'password2',
		'email',
		'firstname',
		'lastname',
		'gender',
		'image'
		]
		extra_kwargs = {"password1":{"write_only":True},"password2":{"write_only":True}}


	def validate(self,data):
		username = data['username']
		email = data['email']
		user_qs = User.objects.filter(username=username)
		user_qs2 = User.objects.filter(email=email)
		if user_qs.exists() or user_qs2.exists():
			raise ValidationError("This user already exists")
		return data

	def validate_password2(self,value):
		data = self.get_initial()
		password1 = data.get("password")
		password2 = value
		if password1 != password2:
			raise ValidationError("Passwords do not match")
		return value

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		try:
			firstname = validated_data['firstname']
		except:
			firstname = ''
		try:
			lastname = validated_data['lastname']
		except:
			lastname = ''
		gender = validated_data['gender']
		try:
			image = validated_data['image']
		except:
			image = None
		user = User(username = username,email=email)
		user.set_password(password)
		user.save()
		if image is not None:
			prof = Profile.objects.create(user=user,email=email,firstname=firstname,lastname=lastname,gender=gender,image=image)
		else:
			prof = Profile.objects.create(user=user,email=email,firstname=firstname,lastname=lastname,gender=gender)
		prof.save()
		return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
	token = serializers.CharField(allow_blank=True,read_only=True)
	username = serializers.CharField(allow_blank=True,required=False)
	password = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
        label = "Password"
    )
	class Meta:
		model = User
		fields = [
		'username',
		'password',
		'token'
		]
		extra_kwargs = {"password":{"write_only":True}}


	def validate(self,data):
		username = data.get("username")
		password = data["password"]
		user = User.objects.filter(username=username).first()
		if user is not None:
			if not user.check_password(password):
				raise ValidationError("Incorrect Credentials.")
			return data
		raise ValidationError("Invalid data")


##############################################################################################################################



class ProfileSerializer(serializers.ModelSerializer):
	firstname = serializers.CharField(label = "First Name",required=True)
	lastname = serializers.CharField(label = "Last Name",required=True)
	class Meta:
		model = Profile
		fields = [
			'image',
			'gender',
			'firstname',
			'lastname'
		]
