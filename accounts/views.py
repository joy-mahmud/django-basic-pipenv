from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.
# from django.contrib.auth.models import User
# from django import forms
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {
#             'username': None,  # Remove the "150 characters or fewer" help text
#             'password1': None,  # Remove default password help text
#             'password2': None,
#         }
        
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['password'].help_text = None
#             self.fields['password'].help_text = None
        
        
        
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
        return render(request,'accounts/register.html')
    
def signIn(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('account_home') 
        
        
    form=AuthenticationForm()
    context={
        "form":form
    }
    return render(request,'accounts/login.html',context=context)
    
