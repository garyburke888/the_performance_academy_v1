from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Setting(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Day(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Class(models.Model):

    class Meta:
        verbose_name_plural = 'Classes'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.CharField(max_length=254)
    setting = models.ForeignKey(
        'Setting', null=True, blank=True, on_delete=models.SET_NULL)
    day = models.ForeignKey(
        'Day', null=True, blank=True, on_delete=models.SET_NULL)
    time = models.CharField(max_length=254)
    teacher = models.CharField(max_length=254)
    term = models.CharField(max_length=254)
    image = models.ImageField()

    def __str__(self):
        return self.name
