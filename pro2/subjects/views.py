from django.shortcuts import render, redirect
from app2.models import Document
from .models import Watch
# Create your views here.

def CseView(request):
    qs= Document.objects.filter(department="cse")
    context={
        "object_list" : qs
    }
    return render(request,"document_list.html",context)

def EceView(request):
    qs= Document.objects.filter(department="ece")
    context={
        "object_list" : qs
    }
    return render(request,"document_list.html",context)

def ITView(request):
    qs= Document.objects.filter(department="it")
    context={
        "object_list" : qs
    }
    return render(request,"document_list.html",context)

def cse_watch(request):
    qs = Watch.objects.filter(department="cse")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def ece_watch(request):
    qs = Watch.objects.filter(department="ece")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def it_watch(request):
    qs = Watch.objects.filter(department="it")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def read(request):
    return render(request,"read.html",{})
