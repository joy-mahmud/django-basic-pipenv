from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document
# Create your views here.

def meidaUpload(request):
    if request.method=="POST":
        form = DocumentForm(request.POST, request.FILES)
      
        if form.is_valid():
            form.save()
            return redirect ('media_upload')
    else:
        form=DocumentForm()
        documents=Document.objects.all()
        return render(request,'mediaUpload/file_upload.html',{'form':form,'documents':documents})