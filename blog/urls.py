from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<category_slug>/', views.category_detail, name='category_detail'),
    # path('<category_slug>/', views.post_list, name='post_list'),
    path('<category_slug>/<post_slug>/', views.post_detail, name='post_detail'),
]
