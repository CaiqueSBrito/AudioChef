from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services.api import recipe_service
from .services.auth.auth_service import authenticate_user, register_user, logout_user

# Create your views here.
def home(request):
    return render(request, 'app_audiochef/index.html')

class RecipesAPIView(APIView):
    def get(self, request):
        data = recipe_service.make_recipe()
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
