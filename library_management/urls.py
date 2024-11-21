from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='library_home'),
    path('addProfile/<int:id>',views.addProfile, name="addProfile"),
    path('testing/',views.testing)
   
]