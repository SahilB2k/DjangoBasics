from django.http import HttpResponse;
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


def home(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is the about page!!")
def store(request):
    return HttpResponse("this is the store page!!")

def Signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print()
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists!")
            return redirect('signup')
        elif pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
        else:       
            my_user=User.objects.create_user(username=username,email=email,password=pass1)
            my_user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        
    return render(request, "login.html")
            



def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"password is incorrect!!")

    return render(request,"signin.html")

def logout(request):
    logout(request)
    return redirect('login')

