from django.urls import path
from story.views import recipes, recipe, like_recipe, get_liked, RecipeListView

app_name = 'story'
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes'),
    path('liked-recipes/', get_liked, name='liked_recipes'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe_single'),
    path('like_recipe/<int:pk>/', like_recipe, name='recipe_like'),
]