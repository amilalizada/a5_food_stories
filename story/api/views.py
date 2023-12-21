from story.models import Category, Recipe
from django.http import JsonResponse
from .serializers import CategoriesSerializer, RecipeReadSerializer, RecipeCreateSerializer
from rest_framework.decorators import api_view

def category_api_view(request):
    categories = Category.objects.all()
    serialized_data = CategoriesSerializer(categories, context={'request': request}, many=True)

    return JsonResponse(serialized_data.data, safe=False)

@api_view(['GET', 'POST'])
def recipe_api_view(request):
    if request.method == "POST":
        serializer = RecipeCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    recipes = Recipe.objects.all()
    serialized_data = RecipeReadSerializer(recipes, context={'request': request}, many=True)

    return JsonResponse(serialized_data.data, safe=False)
