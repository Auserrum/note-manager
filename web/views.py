from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
import time
from .models import Task
import os, json


def index(request):
	if request.user.is_authenticated:
		log = True

		context = {
			'username': User.username,
			'log': log,
			'tasks': Task.objects.filter(user=request.user)
		}

		return render(request=request, template_name='web/index.html', context=context)


	else:
		log = False

		return redirect("login")


def add(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			title = request.POST.get('title')
			user = request.user
			content = request.POST.get('content')

			if title != "" and content != "":
				note = Task.objects.create(user=user, title=title, content=content)

			return redirect('index')

	else:
		return redirect("login")

def completed(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			task = Task.objects.filter(id=id)
			task.delete()

			return redirect('index')

	else:
		return redirect("login")

def logout_view(request):
	logout(request)

	return redirect("index")
