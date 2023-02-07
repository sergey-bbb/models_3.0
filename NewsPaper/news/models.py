# NEWS

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    Author1 = models.CharField(max_length=255)
    Author2 = models.CharField(max_length=255)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Category(models.Model):
    name = models.CharField(unique = True, max_length=255)

class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    Article = models.CharField(max_length=255)
    News = models.CharField(max_length=255)
    About_everything_new = models.CharField(max_length=255, null=True)


    categories = models.ManyToManyField(Category, through = 'PostCategory')

class PostCategory(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)

    comment = models.TextField(default = "Нет комментов")
    comments = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentss = models.ForeignKey(User, on_delete=models.CASCADE, null=True)





