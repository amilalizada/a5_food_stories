# Generated by Django 4.2.6 on 2023-12-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_recipe_options_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_az',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_az',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_ru',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
