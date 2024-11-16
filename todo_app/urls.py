from django.urls import path
from . import views 
urlpatterns =[
    path('',views.TaskView,name='task_list'),
    path('<int:id>/',views.task_details,name="task_details"),
    path('update/<int:id>',views.update_task,name="update_task")
]