from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
	context = {
	}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Login Succesful")
			return redirect("home")
		else:
			messages.success(request, "Login Error")
			return redirect("home")
	else:
		return render(request, "home.html", context)

def login_user(request):
	pass

def logout_user(request):
	pass