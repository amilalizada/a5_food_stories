from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.files import ImageField

User = get_user_model()

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = ImageField(upload_to='media/category')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        # ordering = ['-id']

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = ImageField(upload_to='recipe', null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Recipes'
        verbose_name = 'Recipe'
        # ordering = ['-id']


    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=50)
    image = ImageField(upload_to='story')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class StoryImages(models.Model):
    image = ImageField(upload_to='story/related_images')
    story = models.ForeignKey(Story, on_delete=models.CASCADE)