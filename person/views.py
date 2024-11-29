from django.shortcuts import render
from django.http import HttpResponse
from .models import personCollection,printCollection

# Create your views here.

def home(request):
    printCollection()
    return HttpResponse('<h2>django server is running</h2>')
def add_person(request):
    record=[
        {
        "name":'john',
        "email":'john@gmail.com'
        
        },
        {
         "name":'doe',
         "email":'doe@gmail.com'   
        }
        
    ]
    personCollection.insert_many(record)
   
    
    return HttpResponse('person record added successfully')