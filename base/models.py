from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    created_on = models.DateTimeField(null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    created_on = models.DateTimeField(null=True)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=2)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    pubdate = models.DateField()
    created_on = models.DateTimeField(null=True)

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    created_on = models.DateTimeField(null=True)