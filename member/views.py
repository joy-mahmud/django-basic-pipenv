from django.shortcuts import render
from django.http import HttpResponse
from member.models import Member

# Create your views here.

def home(request):
    mymembers=Member.objects.all().values()
    context={
        mymembers:mymembers
    }
    return render(request,'home.html',context)

def add_member(request):
    member= Member(firstname="joy",lastname='mahmud')
    member.save()
    
    return HttpResponse('member added successfully')
