from django.db import models
from category.models import Category

# Create your models here.
class Card(models.Model):
    brand = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/')
 
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commnet by {self.name}"
    