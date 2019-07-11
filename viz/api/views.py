from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		DestroyAPIView,
		UpdateAPIView,
		RetrieveAPIView
	)
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException, ParseError
from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly
	)
from django.contrib.auth import login, logout
from viz.models import *
from viz.forms import *
from .serializers import *
from .permissions import *
from rest_framework.renderers import ( 
	JSONRenderer,
	TemplateHTMLRenderer,
	BrowsableAPIRenderer
	)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.authentication import (
	TokenAuthentication,
	SessionAuthentication,
	BaseAuthentication
	)
from rest_framework.parsers import FormParser,MultiPartParser
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class AlbumListAPIView(ListAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiAlbumList.html"
	def get_queryset(self):
		return Album.objects.filter(owner=self.request.user)

	serializer_class = 	AlbumListSerializer

	def get(self, request):
		queryset = Album.objects.filter(owner=self.request.user).order_by('-date_posted')
		return Response({'album':queryset})

class AlbumDetailAPIView(RetrieveAPIView):

	"""
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
	"""
	def get_queryset(self):
		return Album.objects.filter(owner=self.request.user)
	serializer_class = AlbumDetailSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiAlbumDetails.html"

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		album=Album.objects.filter(albumid=key).first()
		qs = Photo.objects.filter(albumid=album)
		return Response({'album':album,'photo':qs})


class AlbumUpdateAPIView(LoginRequiredMixin, UserPassesTestMixin, UpdateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumUpdateSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	parser_classes = (MultiPartParser,FormParser, )
	permission_classes = [AllowAny]
	renderer_classes = (TemplateHTMLRenderer,)
	model = Album
	template_name = 'HTML/apiAlbumCreate.html'
	fields = ['title', 'description','cover']

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		album = Album.objects.filter(albumid=key).first()
		form=AlbumCreationForm(request.POST,request.FILES,instance=album)
		context={'form':form,'album':album}
		return Response(context)

	def post(self, request, *args, **kwargs):
		key = kwargs['pk']
		album = Album.objects.filter(albumid=key).first()
		form=AlbumCreationForm(request.POST,request.FILES,instance=album)
		if form.is_valid():
			form.instance.owner = request.user
			form.save()
			messages.success(request,f'Your Album has been Updated!')
			return redirect('viz-api-albumList')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		album = self.get_object()
		if self.request.user == album.owner:
			return True
		return False

class AlbumDeleteAPIView(DestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumDetailSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiAlbumDelete.html"

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		album = Album.objects.filter(albumid=key).first()
		context={'object':album}
		return Response(context)

	def post(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		messages.info(request,f'Your Album has been Deleted!')
		return redirect('viz-api-albumList')

class AlbumCreateAPIView(CreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumCreateSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	parser_classes = (MultiPartParser,FormParser, )
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiAlbumCreate.html"

	def get(self, request):
		form=AlbumCreationForm(request.POST,request.FILES,instance=Album())
		context={'form':form}
		return Response(context)

	def post(self, request, *args, **kwargs):
		form=AlbumCreationForm(request.POST,request.FILES,instance=Album())
		if form.is_valid():
			form.instance.owner = request.user
			form.save()
			messages.success(request,f'Your Album has been created!')
			return redirect('viz-api-albumList')

	def perform_create(self, serializer):
		owner=self.request.user
		image = self.request.data.get('cover')
		serializer.save(owner=owner,cover=image)



############################################################################################################################


class PhotoDeleteAPIView(DestroyAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = PhotoDetailSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiPhotoDelete.html"

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('photos/')
		i=i+7
		key=url[i:i+36:1]
		photo = Photo.objects.filter(photoid=key).first()
		context={'object':photo}
		return Response(context)

	def post(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		messages.info(request,f'Your Album has been Deleted!')
		return redirect('viz-api-albumList')

class PhotoListAPIView(ListAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = 	PhotoListSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	

class PhotoDetailAPIView(RetrieveAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = PhotoDetailSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiPhotoDetails.html"

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('photos/')
		i=i+7
		key=url[i:i+36:1]
		photo=Photo.objects.filter(photoid=key).first()
		return Response({'photo':photo})

class PhotoUpdateAPIView(UpdateAPIView):
	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)
	serializer_class = PhotoUpdateSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	renderer_classes = (TemplateHTMLRenderer,)
	model = Photo
	template_name = 'HTML/apiPhotoCreate.html'
	fields = ['description']

	def get(self, request, *args, **kwargs):
		url=self.request.build_absolute_uri()
		i = url.index('photos/')
		i=i+7
		key=url[i:i+36:1]
		photo = Photo.objects.filter(photoid=key).first()
		form=PhotoUpdateFormInAlbumAPI(instance=Photo())
		context={'form':form,'photoid':photo.photoid}
		return Response(context)

	def post(self, request, *args, **kwargs):
		key=kwargs['pk']
		photo = Photo.objects.filter(photoid=key).first()
		form=self.get_serializer(data=request.data,instance=photo)
		if form.is_valid():
			self.perform_create(form)
			form.save()
			messages.success(request,f'Your Photo has been Updated!')
			return redirect('viz-api-photoDetails',form.instance.photoid)
		return Response(HTTP_400_BAD_REQUEST)

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		album = self.get_object()
		if self.request.user == album.owner:
			return True
		return False

	def perform_create(self, serializers):
		description = self.request.data.get('description')
		serializers.save(description=description)

class PhotoCreateAPIView(CreateAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoCreateSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated, ]
	parser_classes = (MultiPartParser,FormParser, )
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = "HTML/apiPhotoCreate.html"

	def get_form_kwargs(self):
		kwargs = super(PhotoCreateAPIView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		url=self.request.build_absolute_uri()
		i=url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		kwargs['albumid'] = key
		return kwargs

	def perform_create(self, serializers):
		owner=self.request.user
		image = self.request.data.get('image')
		serializers.save(owner=owner,image=image)

	def get(self, request, *args, **kwargs):
		kwargs['user'] = self.request.user
		url=self.request.build_absolute_uri()
		i=url.index('albums/')
		i=i+7
		key=url[i:i+36:1]
		kwargs['albumid'] = key
		form=PhotoFormInAlbumAPI(kwargs=kwargs)
		context={'form':form,'albumid':key}
		return Response(context)

	def post(self, request, *args, **kwargs):
		kwargs=kwargs
		form=self.get_serializer(data=request.data)
		if form.is_valid():
			self.perform_create(form)
			form.save()
			messages.success(request,f'Your Photo has been Uploaded!')
			return redirect('viz-api-albumDetails',form.instance.albumid.albumid)
		return Response(HTTP_400_BAD_REQUEST)



############################################################################################################################




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
	authentication_classes = (TokenAuthentication, SessionAuthentication, )

	def post(self, request, *args, **kwargs):
		try:
			request.user.auth_token.delete()
		except AttributeError:
			return Response(status=HTTP_403_FORBIDDEN)
		logout(request)
		return Response(status=HTTP_204_NO_CONTENT)

