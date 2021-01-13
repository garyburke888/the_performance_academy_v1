from django.db import models
from datetime import datetime

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
