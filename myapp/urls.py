from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.myappHome),
    path('about/',views.about),
    path('profile/',views.profile),
    path('addBook/',views.add_book),
    path('allbooks/',views.display_books),
    path('updateBook/',views.update_book),
    path('deletebook/',views.delete_book)
    ]