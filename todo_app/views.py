from django.shortcuts import render
from .models import Task
def TaskView(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html',{"tasks":tasks})
# Create your views here.
