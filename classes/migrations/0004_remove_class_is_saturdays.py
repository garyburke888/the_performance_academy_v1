# Generated by Django 3.1.4 on 2020-12-31 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20201228_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='is_saturdays',
        ),
    ]
