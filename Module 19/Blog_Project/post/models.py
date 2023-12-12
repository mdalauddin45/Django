from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) #akta post multiple categorir moddhy takty pary abr akta categorir moddhy multiple post takty pary
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/media/uploads/', blank=True, null=True)
 
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()#multiple comment korty parby na cz unique is True
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True) # auto date hisab kory niby 
    
    def __str__(self):
        return f"Commnet by {self.name}"
    