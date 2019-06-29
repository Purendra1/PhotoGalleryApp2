from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'HTML/albumList.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'album'
    ordering = ['-date_posted']


class AlbumDetailView(LoginRequiredMixin, DetailView):
	model=Album
	template_name = 'HTML/showAlbum.html'
	ordering = ['-date_posted']
	def get_context_data(self, **kwargs):
		context = super(AlbumDetailView, self).get_context_data(**kwargs)
		context['photo'] = Photo.objects.filter(owner=context['album'].owner)
		return context


class PhotoDetailView(LoginRequiredMixin, DetailView):
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
			
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				email=request.POST['email']
				messages.success(request,f'Your Profile has been created')

				return respNI(request)
			else:
				messages.warning(request,f'Invalid Form')
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

@login_required
def AlbumCreateView(request):
		
	if(request.method) =='POST':
		form=AlbumCreationForm(request.POST,request.FILES,instance=Album())
		if form.is_valid():
			form.instance.owner = request.user
			form.save()
			messages.success(request,f'Your Album has been created!')
			return redirect('viz-profile')

	else:
		form=AlbumCreationForm(request.POST,request.FILES,instance=Album())
		context={'form':form}
		return render(request,'HTML/albumCreateForm.html',context)
	

class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Album
	template_name = 'HTML/albumCreateForm.html'
	fields = ['title', 'description','cover']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		album = self.get_object()
		if self.request.user == album.owner:
			return True
		return False

class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model=Album
	template_name = 'HTML/albumDelete.html'
	success_url = '/albums'
	success_message = 'Your Album has been deleted!'
	def test_func(self):
		album = self.get_object()
		if self.request.user == album.owner:
			return True
		return False

class PhotoCreateView(LoginRequiredMixin, CreateView):
		model=Photo
		template_name = 'HTML/photoCreateForm.html'
		form_class = PhotoForm

		def form_valid(self, form):
			form.instance.owner = self.request.user
			return super().form_valid(form)

		def get_form_kwargs(self):
			kwargs = super(PhotoCreateView, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs