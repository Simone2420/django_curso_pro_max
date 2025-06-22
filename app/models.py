from re import A
from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    def __str__(self):
        return self.name
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.PROTECT)
    website = models.URLField()
    biography = models.TextField(max_length=500)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #CASCADE ERASE ALL THE BOOKS FROM THE PUBLISHER / DONOTHING / PROTECTED / SET_NULL
    authors = models.ManyToManyField(Author,related_name="authors")

    def __str__(self):
        return self.title

#Authors.objects.all() get all authors
#Author.objects.get(id=1) get author by id
#Author.objects.create(name="Author 1", birth_date="1990-01-01") create author and return it
#Author.objects.filter(name="Author 1") filter authors by name
#Author.objects.filter(birth_date__year=1990) filter authors by birth date
#Author.objects.filter(books__title="Book 1").delete() delete author by book title
#Author.objects.filter(books__title="Book 1").update(name="Book 2") update author by book title
#Author.objects.filter(books__title="Book 1").update(books__title="Book 2") update book by author
#Author.objects.order_by("name") order by name
