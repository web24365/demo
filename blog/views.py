from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Post, Comment

# Create your views here.
class CategoryListView(ListView):
    model = Category

category_list = CategoryListView.as_view()


class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

post_detail = PostDetailView.as_view()
