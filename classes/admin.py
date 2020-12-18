from django.contrib import admin
from .models import Class, Category, Setting, Age

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'age',
        'setting',
        'teacher',
        'price',
        'term',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SettingAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AgeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Class, ClassAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Age, AgeAdmin)
