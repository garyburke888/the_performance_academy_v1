from django.contrib import admin
from .models import Class, Category, Setting, Day

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'age',
        'setting',
        'day',
        'time',
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


class DayAdmin(admin.ModelAdmin):
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
admin.site.register(Day, DayAdmin)
