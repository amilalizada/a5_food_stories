from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from story.models import Recipe, Category
from .forms import CreateRecipeForm

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
    paginate_by = 2
    ordering = '-id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('cat'):
            return queryset.filter(category__id=self.request.GET.get('cat'))
        
        return queryset
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'
    context_object_name = 'recipe'
    redirect_field_name = 'account:login'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context
    

class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'create_recipe.html'
    success_url = reverse_lazy('story:recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('story:recipes')


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'confirm.html'
    success_url = reverse_lazy('story:recipes')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()

    #     return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == self.request.user:
            self.object.delete()
            
        return self.post(request, *args, **kwargs)


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
