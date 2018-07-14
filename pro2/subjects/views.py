from django.shortcuts import render
from app2.models import Document

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
