from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def index(request):
	return render(request=request, template_name='auth/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are successful login, {username}!')
            return redirect('index')
        else:
            messages.error(request, f'Occured an error!')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})