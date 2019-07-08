from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		DestroyAPIView,
		UpdateAPIView,
		RetrieveAPIView
	)

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly
	)
from viz.models import *
from .serializers import *
from .permissions import *
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser,MultiPartParser

class AlbumListAPIView(ListAPIView):
	def get_queryset(self):
		return Album.objects.filter(owner=self.request.user)

	serializer_class = 	AlbumListSerializer

class AlbumDetailAPIView(RetrieveAPIView):

	'''
	def get_queryset(self):
		url=self.request.build_absolute_uri()
		i = url.index('album/')
		i=i+6
		key=url[i:i+36:1]
		album=Album.objects.filter(albumid=key).first()
		qs = Photo.objects.filter(albumid=album)
		for p in qs:
			print(p.albumid)
		return qs
	'''
	queryset = Album.objects.all()
	serializer_class = AlbumDetailSerializer


class AlbumUpdateAPIView(UpdateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumUpdateSerializer
	permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class AlbumDeleteAPIView(DestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumDetailSerializer

class AlbumCreateAPIView(CreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumCreateSerializer
	permission_classes = [IsAuthenticated]
	parser_classes = (MultiPartParser,FormParser, )

	def perform_create(self, serializers):
		owner=self.request.user
		image = self.request.data.get('cover')
		serializers.save(owner=owner,cover=image)




class PhotoDeleteAPIView(DestroyAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
		permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
	serializer_class = PhotoDetailSerializer

class PhotoListAPIView(ListAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = 	PhotoListSerializer

class PhotoDetailAPIView(RetrieveAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = PhotoDetailSerializer

class PhotoUpdateAPIView(UpdateAPIView):
	def get_queryset(self):
		return Album.objects.filter(owner=self.request.user)
	serializer_class = PhotoUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]

class PhotoCreateAPIView(CreateAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoCreateSerializer
	permission_classes = [IsAuthenticated]
	parser_classes = (MultiPartParser,FormParser, )

	def perform_create(self, serializers):
		owner=self.request.user
		image = self.request.data.get('image')
		serializers.save(owner=owner,cover=image)