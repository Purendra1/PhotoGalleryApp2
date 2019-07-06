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

class AlbumListAPIView(ListAPIView):
	queryset = Album.objects.all()
	serializer_class = 	AlbumSerializer

class AlbumDetailAPIView(RetrieveAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class AlbumUpdateAPIView(UpdateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumUpdateSerializer
	permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class AlbumDeleteAPIView(DestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class AlbumCreateAPIView(CreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumCreateSerializer
	permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

	def perform_create(self, serializers):
		serializer.save(owner=self.request.user)



class PhotoDeleteAPIView(DestroyAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer

class PhotoListAPIView(ListAPIView):
	queryset = Photo.objects.all()
	serializer_class = 	PhotoSerializer

class PhotoDetailAPIView(RetrieveAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer

class PhotoUpdateAPIView(UpdateAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]

class PhotoCreateAPIView(CreateAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoCreateSerializer
	permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

	def perform_create(self, serializers):
		serializer.save(owner=self.request.user)