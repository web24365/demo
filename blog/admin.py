from django.contrib import admin
# from django.db import models
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'title', 'text']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message']