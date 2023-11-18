from django.shortcuts import render
from story.models import Recipe

# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes.html', context=context)

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'single.html', context=context)
