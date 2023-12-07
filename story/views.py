from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from story.models import Recipe, Category

# Create your views here.

def recipes(request):
    print(request.session.get('liked_recipes'))
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories
    }
    return render(request, 'recipes.html', context=context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'single.html', context=context)

def like_recipe(request, pk):
    liked_recipes = request.session.get('liked_recipes', '')
    liked_recipe_list = liked_recipes.strip().split(' ')
    if not str(pk) in liked_recipe_list:
        liked_recipes += str(pk) + ' '
    # request.set_cookie('liked_recipes', liked_recipes)
    request.session['liked_recipes'] = liked_recipes

    messages.add_message(request, messages.SUCCESS, "Message sent successfully")

    return redirect('recipes')


def get_liked(request):
    ids = request.session.get('liked_recipes', '')
    if ids:
        ids = ids.strip().split(' ')
        recipes = Recipe.objects.filter(id__in=ids)
        context = {
            'recipes': recipes
        }
        return render(request, 'liked.html', context)

    
    return render(request, 'recipes.html')
