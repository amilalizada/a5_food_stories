from django.shortcuts import render, redirect
from django.contrib import messages
from story.models import Recipe

# Create your views here.

def recipes(request):
    print(request.session.get('liked_recipes'))
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
