from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="some desc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Books, related_name="authors")
    notes = models.TextField(default="some notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)