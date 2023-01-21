# Generated by Django 4.1.5 on 2023-01-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storecatalog', '0003_genre_delete_publisher_book_sale_currency_book_sku_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a publisher name, e.g., Penguin publishers', max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('publisher_id', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='publisher_id',
            new_name='genre_id',
        ),
    ]