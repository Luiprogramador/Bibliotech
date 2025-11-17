from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class  Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True, help_text="13 Character ISBN number")
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title
# Create your models here.
