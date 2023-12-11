from django.urls import path
from story.views import recipes, recipe, like_recipe, get_liked, RecipeListView, RecipeDetailView, CreateRecipeView, UpdateRecipeView, DeleteRecipeView

app_name = 'story'
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes'),
    path('liked-recipes/', get_liked, name='liked_recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_single'),
    path('like-recipe/<int:pk>/', like_recipe, name='recipe_like'),
    path('create-recipe/', CreateRecipeView.as_view(), name='create_recipe'),
    path('update-recipe/<int:pk>/', UpdateRecipeView.as_view(), name='update_recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipeView.as_view(), name='delete_recipe'),
]