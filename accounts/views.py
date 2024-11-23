from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):
    if request.method=="POST":
        form =UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_home')
    else:
        form=UserCreationForm()
        context={
            "form":form
        }
        return render(request,'accounts/register.html',context)
    
