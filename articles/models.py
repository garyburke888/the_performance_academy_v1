from django.db import models
from datetime import date


class Article(models.Model):
    author = ('The Performance Academy')
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(default=date.today)
    image = models.ImageField(default='noimage2.png')

    def __str__(self):
        return self.title
