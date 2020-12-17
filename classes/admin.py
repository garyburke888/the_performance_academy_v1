from django.contrib import admin
from .models import Class, Category, Setting

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


admin.site.register(Class, ClassAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Setting, SettingAdmin)
