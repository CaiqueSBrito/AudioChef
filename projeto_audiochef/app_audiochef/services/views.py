from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.http import JsonResponse

from ..models import Recipe
from ..serializers import RecipeSerializer

from .api import recipe_maker_service
from .api.random.spoonacular_random_client import SpoonacularRandomClient
from .api.search import search_recipes
from .api.search.spoonacular_search_client import SpoonacularSearchClient
from .auth.auth_service import authenticate_user, register_user, logout_user

# Create your views here.
def home(request):
    return render(request, 'app_audiochef/index.html')

def search_page(request):
    return render(request, 'app_audiochef/search.html')

def crud_page(request):
    return render(request, 'app_audiochef/crud_receitas.html')

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRandomAPIView(APIView):
    def get(self, request):
        client = SpoonacularRandomClient()
        data = recipe_maker_service.make_recipe(client)
        return Response(data, status=status.HTTP_200_OK)

class RecipeSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        client = SpoonacularSearchClient()
        data = search_recipes.make_list(client, query)
        return Response(data, status=status.HTTP_200_OK)

class RecipeDetailAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        client = SpoonacularDetailClient()
        data = detail_recipe.make_detail(client, query)
        return Response(data, status=status.HTTP_200_OK)

def entrar(request):
    if request.method == 'POST':
        token, erro = authenticate_user(request)
        if erro:
            return JsonResponse({'erro': erro}, status=400)
        return JsonResponse({'ok': True, 'token': token})
    return render(request, 'app_audiochef/login.html')

def registro(request):
    if request.method == 'POST':
        token, erro = register_user(request)
        if erro:
            return JsonResponse({'erro': erro}, status=400)
        return JsonResponse({'ok': True, 'token': token})
    return render(request, 'app_audiochef/registro.html')

def sair(request):
    logout_user(request)
    return redirect('login')
