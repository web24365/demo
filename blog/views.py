from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Post, Comment

# Create your views here.
class CategoryListView(ListView):
    model = Category

category_list = CategoryListView.as_view()

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    slug_url_kwarg = 'category_slug'

category_detail = CategoryDetailView.as_view()


# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     # slug_url_kwargs = 'category_slug'

#     def get_context_data(self, object_list=None, **kwargs):
#         category_list = Category.objects.all()
#         # context['category_list'] = Category.objects.all()
#         return super().get_context_data(category_list=category_list, **kwargs)

#     def get_queryset(self):
#         self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
#         return Post.objects.filter(category=self.category)
#         # queryset = Post.objects.filter(category=self.kwargs['category'])
#         # return super().get_queryset()
#         # def get_queryset(self):
#         # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
#         # return Book.objects.filter(publisher=self.publisher)

# post_list = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

post_detail = PostDetailView.as_view()
