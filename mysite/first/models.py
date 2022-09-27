from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(default='')
