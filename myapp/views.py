from django.shortcuts import render
from django.http import HttpResponse
def myappHome(req):
    return render(req,'index.html',{"title":'home','content':'This is home content'})
def about(request):
    page={
        'title':'about',
        'content':'This is about page content'
    }
    return render(request,'about.html',page)
def profile(request):
     social =['facebook:me.facebook.com','github:me.github.com','instagram:me.instagram.com']
     return render(request,'profile.html',{'title':'profile','social':social})
# Create your views here.
