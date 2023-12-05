from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) #akta post multiple categorir moddhy takty pary abr akta categorir moddhy multiple post takty pary
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
 