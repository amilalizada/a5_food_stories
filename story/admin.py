from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import Category, Tag, Recipe, Story, StoryImages


# Register your models here.

admin.site.register(Tag)
admin.site.register(StoryImages)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'get_photo', 'slug', 'category', 'content', 'description', 'get_tags', 'created_at',)
    list_filter = ["category", "author", "tags"]
    list_display_links = ['title', 'content']
    list_editable = ['category', 'author',]
    search_fields = ['title', 'content', 'description', 'category__title', 'tags__title']
    fieldsets = (
        ('info', {
            'fields': ('title', 'image', 'content', 'description', 'slug')
        }),
        ('relations', {
            'fields': ('category', 'tags', 'author',)
        }),
    )

    def get_tags(self, obj):
        tag_arr = [p.title for p in obj.tags.all()]

        return tag_arr
    
    def get_photo(self, obj):
        if obj.image:
            img_str = f"<img src='{obj.image.url}' width='100px'>"
        return format_html(img_str)
    

class ImageInline(admin.TabularInline):
    model = StoryImages
    extra = 2


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
        

