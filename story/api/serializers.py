from rest_framework import serializers
from story.models import Category, Recipe, Tag

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
        )


class RecipeTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'title',
        )


class RecipeReadSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    tags = RecipeTagSerializer(many=True)
    author = serializers.CharField(source='author.get_full_name')
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'image',
            'description',
            'content',
            'category',
            'tags',
            'author',
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'content',
            'description',
            'image',
            'category',
            'tags',
            'author',
        )

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     print(self.context["request"].user)
    #     # instance.author = self.context['request'].user
    #     # if commit:
    #     #     instance.save()
    #     return instance
