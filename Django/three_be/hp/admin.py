from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Post
from .forms import BlogForm, PostForm
# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    form = BlogForm


class PostAdmin(SummernoteModelAdmin):
    form = PostForm


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)