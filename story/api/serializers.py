from rest_framework import serializers
from story.models import Category, Recipe, Tag
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username

        return token

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
        )


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
        )


class RecipeTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'title',
        )


class RecipeReadSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.title')
    category = CategoriesSerializer()
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
    author = serializers.PrimaryKeyRelatedField(read_only=True)
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
    
    def validate(self, attrs):
        attrs['author'] = self.context["request"].user

        return super().validate(attrs)

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     print(self.context["request"].user)
    #     # instance.author = self.context['request'].user
    #     # if commit:
    #     #     instance.save()
    #     return instance
