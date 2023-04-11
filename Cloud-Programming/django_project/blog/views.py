from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

from .models import Post, Category, Tag


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'sub_title', 'content', 'head_image', 'file_upload', 'category', 'tag']
    #업데이트 할 필드만 써주기
    template_name="blog/post_form_update.html"

    def dispatch(self, request, *args, **kwargs):
        # update 권한 O
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)  # 원래 하려던걸 해라.
        else:
            raise PermissionDenied


class PostCreate(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'sub_title', 'content', 'head_image', 'file_upload', 'category', 'tag']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and current_user.is_staff or current_user.is_superuser:
            form.instance.author = current_user  # form의 author 자리에 user할당
            return super(PostCreate, self).form_valid(form)  # postcreate로부터 form_vaild 수행해라
        else:
            return redirect('/blog/')


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


# FBV로 해당 카테고리를 가진 post_list 출력하는 페이지 만들기
def categories_page(request, slug):
    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)

    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories': Category.objects.all(),
        'no_category_count': Post.objects.filter(category=None).count(),
        'category': category,
        'post_list': post_list,
    }

    return render(request, 'blog/post_list.html', context)


# FBV로 해당 태그를 가진 post_list 출력하는 페이지 만들기
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()  # m_to_m 으로 set
    # template 에 넘겨줄 context
    context = {
        'categories': Category.objects.all(),
        'no_category_count': Post.objects.filter(category=None).count(),
        'post_list': post_list,
        'tag': tag,
    }

    return render(request, 'blog/post_list.html', context)
