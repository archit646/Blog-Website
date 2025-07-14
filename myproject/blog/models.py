from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to='images/',default="")
    def __str__(self):
        return self.title
    
