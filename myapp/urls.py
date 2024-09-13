from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.myappHome),
    path('about/',views.about),
    path('profile/',views.profile),
    ]