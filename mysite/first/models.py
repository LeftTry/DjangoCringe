from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    bday = models.DateField('date born')

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    num_pages = models.IntegerField(default=0)
    text = models.TextField(default='')
