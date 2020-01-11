from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, db_index=True, unique=True, allow_unicode=True, null=True)

    def __str__(self):
        # 해당 model을 참조할 때 표시되는 필드를 지정
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category_detail", kwargs={"pk": self.pk})
    

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    # 아래의 방법을 추천(AUTH_USER_MODEL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    