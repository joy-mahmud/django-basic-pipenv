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
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Many-to-one
    published_date = models.DateField()

    def __str__(self):
        return self.title
