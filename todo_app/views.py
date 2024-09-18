from django.shortcuts import render
from .models import Task
def TaskView(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html',{"tasks":tasks})

def task_details(req,id):
    task = Task.objects.get(pk=id)
    return render(req,'task_details.html',{"task":task})
