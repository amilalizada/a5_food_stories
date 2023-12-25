from rest_framework.routers import DefaultRouter
from story.api.views import RecipeViewSet

router = DefaultRouter()

router.register(r'recipes', RecipeViewSet, basename='recipes')