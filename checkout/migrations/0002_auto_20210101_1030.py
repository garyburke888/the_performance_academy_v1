# Generated by Django 3.1.4 on 2021-01-01 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='a_class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='class_day',
            new_name='day',
        ),
    ]