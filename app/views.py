from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,redirect
from app.forms import *
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
def signinpage(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"registration successfull 🤩 "  + user)
            return redirect('loginpage')
    context={
        'form':form
        }
    return render (request,'signup.html',context)
def loginpage(request):
   
    if request.method == 'POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull 🤗")
            return redirect('home')
        else:
            messages.info(request,"Please check the username and password 😐")
            return redirect('loginpage')
    return render (request,'loginpage.html')
def logoutpage(request):
    logout(request)
    messages.success(request,"you have been successfully logged out from this page 😊 ")
    return redirect('loginpage')
def home(request):
    return render(request,'home.html')
