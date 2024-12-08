from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.meidaUpload,name='media_upload')
]
