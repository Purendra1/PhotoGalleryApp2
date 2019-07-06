from rest_framework import serializers
from viz.models import *

class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'date_posted',
			'owner',
			'cover'
		]
		
class AlbumUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'cover'
		]
		
class AlbumCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields = [
			'title',
			'description',
			'cover'
		]







class PhotoCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields = [
			'description',
			'albumid',
			'image'
		]


class PhotoSerializer(serializers.ModelSerializer):
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
			'albumid',
		]
		

