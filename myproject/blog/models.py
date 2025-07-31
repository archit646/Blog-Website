from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextField()
    created_at=models.DateField(auto_now_add=True)
    views=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to='images/',default="")
    def __str__(self):
        return self.title
    
