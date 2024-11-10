from django.http import HttpResponse 
from django.shortcuts import render

def app_home(request):
    return render(request,'index.html')