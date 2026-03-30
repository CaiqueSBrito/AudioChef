import requests
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.core.serializers import serialize

def registro(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        email    = body.get('email')
        senha    = body.get('senha')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'erro': 'Email já cadastrado'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=senha)
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'ok': True, 'token': token.key})

    return render(request, 'app_audiochef/registro.html')

def entrar(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body.get('email')
        senha = body.get('senha')

        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            return JsonResponse({'erro': 'Usuário não encontrado'}, status=400)

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'ok': True, 'token': token.key})
        return JsonResponse({'erro': 'Senha incorreta'}, status=400)

    return render(request, 'app_audiochef/login.html')

def sair(request):
    logout(request)
    return redirect('login')