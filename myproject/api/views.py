from django.shortcuts import render
from rest_framework import viewsets
from blog.models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    @action(detail=False,methods=['get'])
    def recent(self,request):
        posts=Post.objects.all().order_by('-created_at')[:5]
        serializer=self.get_serializer(posts,many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=['get'])
    def releated(self,request,pk=None):
        post=self.get_object()
        releated_posts=Post.objects.filter(category=post.category).exclude(id=post.id)[:5]
        serializer=self.get_serializer(releated_posts,many=True)
        return Response(serializer.data)
    
