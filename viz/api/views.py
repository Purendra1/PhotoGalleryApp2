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
from django.contrib.auth import login, logout
from viz.models import *
from .serializers import *
from .permissions import *
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser,MultiPartParser
from django.contrib.auth.models import User



class AlbumListAPIView(ListAPIView):
	authentication_classes = (TokenAuthentication, )
	permission_classes = [IsAuthenticated, ]
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
	def get_queryset(self):
		return Album.objects.filter(owner=self.request.user)
	serializer_class = AlbumDetailSerializer
	authentication_classes = (TokenAuthentication, )
	permission_classes = [IsAuthenticated, ]


class AlbumUpdateAPIView(UpdateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumUpdateSerializer
	authentication_classes = (TokenAuthentication, )
	permission_classes = [IsAuthenticated, ]

class AlbumDeleteAPIView(DestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumDetailSerializer
	authentication_classes = (TokenAuthentication, )
	permission_classes = [IsAuthenticated, ]

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
		return Photo.objects.filter(owner=self.request.user)
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



class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
	

class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			username = new_data["username"]
			user = User.objects.filter(username=username).first()
			login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			return Response({'token': token.key},status=HTTP_200_OK)
		print(serializer.errors)
		return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
	authentication_classes = (TokenAuthentication, )

	def post(self, request, *args, **kwargs):
		logout(request)
		return Response(status=204)

