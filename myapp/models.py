from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=200)
    publish_date=models.DateField()
    isbn_number= models.CharField(max_length=13,unique=True)
    
    def __str__(self):
        return self.title

# Create your models here.
