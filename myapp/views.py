from django.shortcuts import render
from django.http import HttpResponse
def myappHome(request):
    return render(request,'index.html')

# Create your views here.
