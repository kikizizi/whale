from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

class PostList(ListView):
    model=Post

class PostDetail(DetailView):
    model=Post