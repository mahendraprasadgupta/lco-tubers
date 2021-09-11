from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    redirect('home')

def dashboard(request):
    return render(request,'accounts/dashboard.html')