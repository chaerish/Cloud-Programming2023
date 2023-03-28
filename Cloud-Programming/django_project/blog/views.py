from django.views.generic import ListView, DetailView

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

