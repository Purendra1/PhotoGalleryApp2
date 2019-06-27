from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import Context, loader
from .forms import UserRegisterForm
# Create your views here.

def home(request):
	if request.method == 'GET':
		form=UserRegisterForm()
		return render(request,'HTML/signUp.html', {'formSignUp': form})
	else:
		if request.method == 'POST':
			messages.success(request,f'this msd')
			if 'email' in request.POST:
				form = UserRegisterForm(request.POST)
				if form.is_valid():
					email=request.POST['email']
					messages.success(request,f'this msg {email}')
					return respNI(request)
				else:
					form = UserRegisterForm(request.POST)
				return render(request, 'HTML/signUp.html', {'formSignUp': form})
			else:
				username = request.POST['username']
				password = request.POST['password']
				return render(request,'HTML/loginHome.html')



def respNI(request):
	return render(request,'HTML/resp.html')

def showSignUp(request):
	form=UserRegisterForm()
	return render(request,'HTML/signUp.html', {'formSignUp': form})

def showSignIn(request):
	return render(request,'HTML/signIn.html')