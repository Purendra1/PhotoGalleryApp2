from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import Context, loader
# Create your views here.

def home(request):
	if request.method == 'GET':
		return render(request,'HTML/home.html')
	else:
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				if 'email' not in request.POST:
					xyz=6
					messages.success(request,f'this msd')
				else:
					email=request.POST['email']
					messages.success(request,f'this msg {email}')
					return redirect('viz-home')
			else:
				form = UserCreationForm()
		return render(request, 'HTML/resp.html', {'form': form})
