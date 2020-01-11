from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, db_index=True, unique=True, allow_unicode=True, null=True)

    def get_absolute_url(self):
        return reverse("blog:category_detail", kwargs={"pk": self.pk})
    

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    