from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Post


def index(request):
    #사용자의 요청을 받아서 이런일 저런일을...
    posts = Post.objects.all().order_by('-pk')


    return render(request, 'blog/index.html', {
        'posts': posts,
    })


def single_post_page(request, post_num): #글 하나씩 보여주는 거
    post = Post.objects.get(pk=post_num)

    return render(request, 'blog/single_post_page.html', {
        'post': post,
    })