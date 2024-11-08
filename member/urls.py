from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('addMember/',views.add_member)
]
