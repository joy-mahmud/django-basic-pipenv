from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('addPerson/',views.add_person),
    path('allPersons/',views.view_all_person),
    path('personDetails/',views.person_details)
]
