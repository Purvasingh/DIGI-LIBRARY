from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from role.models import Role

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("error")
    context= {
        "form":form
    }
    return render(request,"login.html",context)

def home_page(request):
    qs=None
    try:
        if request.user.is_authenticated:
            qs=Role.objects.get(user=request.user)
    except Role.DoesNotExist:
        qs=None
    context={
        "qs" : qs
    }
    return render(request,"base.html",context)

def logout_page(request):
    logout(request)
    return redirect("login")

def contact_page(request):
    return render(request,"contact.html",{})
