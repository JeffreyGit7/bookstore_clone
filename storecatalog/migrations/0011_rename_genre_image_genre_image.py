# Generated by Django 4.1.5 on 2023-01-21 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storecatalog', '0010_genre_genre_image_publisher_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_image',
            new_name='image',
        ),
    ]