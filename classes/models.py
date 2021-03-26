from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Setting(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Age(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Class(models.Model):

    class Meta:
        verbose_name_plural = 'Classes'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    is_weekdays = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    age = models.ForeignKey(
        'Age', null=True, blank=True, on_delete=models.SET_NULL)
    setting = models.ForeignKey(
        'Setting', null=True, blank=True, on_delete=models.SET_NULL)
    teacher = models.CharField(max_length=254, null=True, blank=True)
    term = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
