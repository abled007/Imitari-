from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(max_length=500, upload_to='images')
    caption = models.TextField()

    def __str__(self):
        return self.title