from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.myappHome),
    path('about/',views.about),
    path('profile/',views.profile),
    path('addBook/',views.insert_data),
    path('allbooks/',views.display_books),
    path('updateBook/',views.update_book)
    ]