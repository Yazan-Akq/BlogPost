from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm, EditProfileForm, EditPasswordForm

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You Have Been Logged In... '))
			return redirect('home')
			
		else:
			messages.success(request, ('Error! Please Try Again...'))
			return redirect('login_user')
	else:	
		return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ('You have Been Logged Out...'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You have Been Registered...'))
			return redirect('home')
	else:
		form = RegisterForm()
	context = {'form': form}	
	return render(request, 'register.html', context)

def EditProfile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
	context = {'form': form}	
	return render(request, 'edit_profile.html', context)

def edit_password(request):
	if request.method == 'POST':
		form = EditPasswordForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = EditPasswordForm(user=request.user)
	context = {'form': form}	
	return render(request, 'edit_password.html', context)