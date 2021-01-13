from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from classes.models import Class

# Create your models here.


class Rating(models.Model):
    class_name = models.ForeignKey(Class, null=False, blank=False, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.pk)
