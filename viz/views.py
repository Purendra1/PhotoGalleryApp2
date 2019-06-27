from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import Context, loader
from .forms import UserRegisterForm
from .models import *
# Create your views here.

def home(request):
	return render(request,'HTML/home.html')


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
				messages.success(request,f'this msg {email}')

				return respNI(request)
			else:
				form = UserRegisterForm(request.POST)
			return render(request, 'HTML/signUp.html', {'form': form})

def showSignIn(request):
	if request.method == 'GET':
		return render(request,'HTML/signIn.html')
	if request.method == 'POST':
			messages.success(request,f'this msd')
			username = request.POST['username']
			password = request.POST['password']
			return render(request,'HTML/loginHome.html')

@login_required
def profile(request):
	return render(request,'HTML/profile.html')
