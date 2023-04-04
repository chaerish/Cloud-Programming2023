from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import os.path
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30, null=True, default='')
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/img/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to="blog/img/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user // cascade= > 계단식으로 다 삭제해라
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE);

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
