# Generated by Django 4.2.3 on 2023-08-01 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopStore', '0002_category_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
    ]
