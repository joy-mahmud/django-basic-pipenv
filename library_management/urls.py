from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='library_home'),
    path('testing/',views.testing)
   
]