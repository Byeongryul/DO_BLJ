from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST' and User.is_active:
        return redirect('/home/')
    else:
        return render(request, 'login.html')