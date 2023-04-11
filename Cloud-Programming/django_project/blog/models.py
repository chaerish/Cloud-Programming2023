from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import os.path
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural='Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'





class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30, null=True, default='', blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
    tag = models.ManyToManyField(Tag)

    head_image = models.ImageField(upload_to='blog/img/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to="blog/img/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user // cascade= > 계단식으로 다 삭제해라
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE);

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

