from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserRegistrationForm

def register_page(request):
	form = UserRegistrationForm()
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login-page')	
	context = {'form': form}
	return render(request, 'user/register.html', context)



def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('blog-home')
		else:
			messages.info(request, "your password or username is incorrect.")	
	context = {}
	return render(request, 'user/login_page.html', context)



@login_required()
def logout_page(request):
	logout(request)
	return redirect('blog-home')	