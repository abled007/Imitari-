from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(max_length=500, upload_to='images')
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=120)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']