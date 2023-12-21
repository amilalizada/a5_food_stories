from django.urls import path
from story.api.views import category_api_view, recipe_api_view

app_name = 'api'
urlpatterns = [
    path('categories/', category_api_view, name='categories'),
    path('recipes/', recipe_api_view, name='recipes'),
]