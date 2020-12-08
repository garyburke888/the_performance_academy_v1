from django.contrib import admin
from .models import Class, Category, Setting, Day

# Register your models here.
admin.site.register(Class)
admin.site.register(Category)
admin.site.register(Setting)
admin.site.register(Day)
