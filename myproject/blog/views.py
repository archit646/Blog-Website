from django.shortcuts import render
from django.views.generic import *
from .models import *

class HomePageView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'
    
