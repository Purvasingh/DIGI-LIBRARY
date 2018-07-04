from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            redirect('login/')
        else:
            print("error")
    context= {
        "form":form
    }
    return render(request,"login.html",context)

def home_page(request):

    return render(request,"base.html",{})
