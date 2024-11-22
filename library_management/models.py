from django.db import models


# Author model (one-to-many with Book)
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Book model (many-to-many with Genre, one-to-many with Author)
class Book(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Many-to-one
    authors = models.ManyToManyField(Author, related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    author= models.OneToOneField(Author,on_delete=models.CASCADE,related_name='profile')
    bio=models.TextField()
    website=models.URLField(blank=True,null=True)
    birthDate=models.DateField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"profile of {self.author.name}"
    

