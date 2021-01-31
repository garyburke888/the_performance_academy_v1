from django.db import models
from datetime import date


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(default=date.today, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
