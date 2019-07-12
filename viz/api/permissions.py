from rest_framework.permissions import *
from viz.models import *

class IsOwnerOrReadOnly(BasePermission):
	message = 'You can\'t edit someone else\'s Objects'
	my_safe_methods = ['GET','PUT']
	def has_permission(self,request,view):
		url=request.build_absolute_uri()
		i=-1
		try:
			i = url.index('photos/')
			i=i+7
			key=url[i:i+36:1]
			obj = Photo.objects.filter(photoid=key).first()
			if request.method in self.my_safe_methods:
				return obj.owner == request.user
			return False
		except:
			print('not a photo')
		try:
			i=url.index('albums/')
			i=i+7
			key=url[i:i+36:1]
			obj = Photo.objects.filter(albumid=key).first()
			if request.method in self.my_safe_methods:
				return obj.owner == request.user
			return False
		except:
			print('not an album')

		if request.method in self.my_safe_methods:
			return True
		return False


	def has_object_permission(self,request,view,obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.owner == request.user
