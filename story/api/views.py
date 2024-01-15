from story.models import Category, Recipe, Tag
from django.http import JsonResponse
from .serializers import CategoriesSerializer, RecipeReadSerializer, RecipeCreateSerializer, TagsSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class RecipeViewSet(ModelViewSet):
    ...
    # serilaizer_class = RecipeReadSerializer
    # serializer_classes = {
    #     'default': RecipeReadSerializer,
    #     'create': RecipeCreateSerializer,
    #     'update': RecipeCreateSerializer,
    #     'read': RecipeReadSerializer
    # }
    # queryset = Recipe.objects.all()

    # def get_serializer_class(self):
    #     if self.action in self.serializer_classes.keys():
    #         self.serializer_class = self.serializer_classes.get(self.action) #create
    #     else:
    #         self.serializer_class = self.serializer_classes['default']
        
    #     return super().get_serializer_class()


class RecipeListCreateAPIView(ListCreateAPIView):
    '''
        This api view is used to create and list recipes
    '''
    serializer_class = RecipeReadSerializer
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__title', 'title']
    search_fields = ['title']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = RecipeCreateSerializer

        return super().get_serializer_class()


class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeReadSerializer
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            self.serializer_class = RecipeCreateSerializer

        return super().get_serializer_class()


def category_api_view(request):
    categories = Category.objects.all()
    serialized_data = CategoriesSerializer(categories, context={'request': request}, many=True)

    return JsonResponse(serialized_data.data, safe=False)


def tag_api_view(request):
    tags = Tag.objects.all()
    serialized_data = TagsSerializer(tags, context={'request': request}, many=True)

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


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def recipe_read_del_upd(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)

    if request.method == 'GET':
        serializer = RecipeReadSerializer(recipe, context={'request': request})
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = RecipeCreateSerializer(recipe, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'message': 'Recipe deleted successfully'}, status=204)
    
    elif request.method == 'PATCH':
        serializer = RecipeCreateSerializer(recipe, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse({'message': 'Something went wrong'}, status=400)