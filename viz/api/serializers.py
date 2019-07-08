from rest_framework import serializers
from viz.models import *
from rest_framework.serializers import (
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from rest_framework import routers
from django.http import JsonResponse

class AlbumListSerializer(serializers.ModelSerializer):
	detail_url = HyperlinkedIdentityField(
		view_name='viz-api:viz-api-albumDetails'
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

	def create(self, validated_data):
		image = validated_data.pop('cover')
		album = Album.objects.create(**validated_data)
		album.cover = image
		return album






class PhotoCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields = [
			'description',
			'albumid',
			'image'
		]

	def create(self, validated_data):
		return Photo.objects.create(**validated_data)

class PhotoListSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='viz-api:viz-api-photoDetails'
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
		

