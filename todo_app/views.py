from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
def TaskView(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html',{"tasks":tasks})

def task_details(req,id):
    task = Task.objects.get(pk=id)
    return render(req,'task_details.html',{"task":task})

def update_task(request,id):
    try:
        task=Task.objects.get(id=id)
        if request.method == "POST":
            task_form=TaskForm(request.POST,instance=task)
            if task_form.is_valid():
                task_form.save()
                return redirect('task_list')
            else:
                task_form=TaskForm(request.POST,instance=task)
                return render(request,'task_update.html',{'form':task_form}) 
        task_form =TaskForm(instance=task)
        return render(request,'task_update.html',{'form':task_form})   
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')
