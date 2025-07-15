from django.shortcuts import render
from django.views.generic import *
from .models import *

class HomePageView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['recent']=Post.objects.order_by('-created_at')[:5]
        context['categories']=Category.objects.all()
        context['trending']=Post.objects.order_by('-views')[:5]
        return context
    def get_queryset(self):
        queryset=Post.objects.all()
        category=self.request.GET.get('category')
        if category:
            queryset=queryset.filter(category__name__iexact=category)
        return queryset
            
    
