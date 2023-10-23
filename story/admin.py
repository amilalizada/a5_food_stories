from django.contrib import admin
from .models import Category, Tag, Recipe, Story

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Story)
