# Generated by Django 3.1.4 on 2021-01-20 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]