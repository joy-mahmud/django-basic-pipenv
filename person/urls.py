from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('addPerson/',views.add_person)
]
