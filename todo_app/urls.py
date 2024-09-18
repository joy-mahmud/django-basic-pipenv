from django.urls import path
from . import views 
urlpatterns =[
    path('',views.TaskView),
    path('<int:id>/',views.task_details,name="task_details"),
]