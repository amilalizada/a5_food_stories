from django.urls import path
from story.api.views import (
    category_api_view, 
    recipe_read_del_upd,
    RecipeListCreateAPIView,
    RecipeRetrieveUpdateDestroyAPIView
)
from story.api.router import router

app_name = 'api'
urlpatterns = [
    path('categories/', category_api_view, name='categories'),
    # path('recipes/', RecipeListCreateAPIView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe'),
]
urlpatterns += router.urls