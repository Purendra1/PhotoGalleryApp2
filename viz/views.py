from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import uuid
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import Context, loader
from .forms import *
from .models import *
# Create your views here.

def home(request):
	return render(request,'HTML/home.html')

class AlbumListView(ListView):
    model = Album
    template_name = 'HTML/albumList.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'album'
    ordering = ['-date_posted']


class AlbumDetailView(DetailView):
	model=Album
	template_name = 'HTML/showAlbum.html'
	ordering = ['-date_posted']
	def get_context_data(self, **kwargs):
		context = super(AlbumDetailView, self).get_context_data(**kwargs)
		context['photo'] = Photo.objects.filter(owner=context['album'].owner)
		return context


class PhotoDetailView(DetailView):
	model=Photo
	template_name = 'HTML/showPhoto.html'
	ordering = ['-date_posted']


def respNI(request):
	return render(request,'HTML/resp.html')

def showSignUp(request):
	if request.method == 'GET':
		form=UserRegisterForm()
		return render(request,'HTML/signUp.html', {'form': form})
	else:
		if request.method == 'POST':
			messages.success(request,f'this msd')
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				email=request.POST['email']
				messages.success(request,f'Your Profile has been created {username}')

				return respNI(request)
			else:
				form = UserRegisterForm(request.POST)
			return render(request, 'HTML/signUp.html', {'form': form})

def showSignIn(request):
	if request.method == 'GET':
		return render(request,'HTML/signIn.html')
	if request.method == 'POST':
			messages.success(request,f'Signed In')
			username = request.POST['username']
			password = request.POST['password']
			return render(request,'HTML/loginHome.html')

@login_required
def profile(request):
	if request.method == 'POST':
		 p_form = ProfileUpateForm(request.POST, request.FILES, instance=request.user.profile)
		 if p_form.is_valid():
		 	p_form.save()
		 	messages.success(request, f'Your profile has been updated!')
		 	return redirect('viz-profile')
	else:
		p_form = ProfileUpateForm(instance=request.user.profile)
		context={
		'p_form' : p_form
		}
		return render(request,'HTML/profile.html',context)

def AlbumCreateView(request):
		
	if(request.method) =='POST':
		form=AlbumCreationForm(request.POST,request.FILES,instance=Album())
		if form.is_valid():
			form.instance.owner = request.user
			form.save()
			messages.success(request,f'Your Album has been created!')
			return redirect('viz-profile')

	else:
		form=AlbumCreationForm()
		context={'form':form}
		return render(request,'HTML/albumCreateForm.html',context)
	