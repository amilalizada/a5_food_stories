# Generated by Django 4.2.6 on 2023-11-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_recipe_options_alter_category_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-id'], 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
    ]