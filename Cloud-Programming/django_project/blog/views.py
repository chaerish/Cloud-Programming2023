from django.views.generic import ListView, DetailView

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Post, Category, Tag


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

def categories_page(request,slug):
    if slug=='no-category':
        category='미분류'
        post_list= Post.objects.filter(category=None)

    else:

        category = Category.objects.get(slug=slug)
        post_list= Post.objects.filter(category=category)


    context= {
        'categories' : Category.objects.all(),
        'no_category_count' : Post.objects.filter(category=None).count(),
        'category': category,
        'post_list': post_list,
    }


    return render(request, 'blog/post_list.html',context)
def tag_page(request,slug):

    tag = Tag.objects.get(slug=slug)
    post_list= tag.post_set.all()


    context= {
        'categories' : Category.objects.all(),
        'no_category_count' : Post.objects.filter(category=None).count(),
        'post_list': post_list,
        'tag':tag,
    }


    return render(request, 'blog/post_list.html',context)