from django.contrib import admin
from django.utils.text import slugify
# from django.db import models
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name']
    actions = ['make_slug']

    def make_slug(self, request, queryset):
        for category in queryset:
            category.slug = slugify(category.name)
            category.save()
            self.message_user(request, "%s successfully make slug" % category.slug)
    make_slug.short_description = "지정 포스팅의 slug를 만듭니다."

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'title', 'slug', 'text']
    fields = ['category', 'title', 'text']
    actions = ['make_slug']

    def make_slug(self, request, queryset):
        for post in queryset:
            post.slug = slugify(post.title)
            post.save()
            self.message_user(request, "%s successfully make slug" % post.slug)
    make_slug.short_description = "지정 포스팅의 slug를 만듭니다."

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message']
    fields = ['post', 'message']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
