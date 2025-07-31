from rest_framework import serializers
from blog.models import *
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()
    category=CategorySerializer()
    class Meta:
        model=Post
        fields='__all__'