from modeltranslation.translator import translator, TranslationOptions
from story.models import Recipe, Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')

translator.register(Category, CategoryTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)