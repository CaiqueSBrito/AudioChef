import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def authenticate_user(request):
    body = json.loads(request.body)
    email = body.get('email')
    senha = body.get('senha')

    try:
        username = User.objects.get(email=email).username
    except User.DoesNotExist:
        return None, 'Email não encontrado'

    user = authenticate(request, username=username, password=senha)
    if not user:
        return None, 'Senha incorreta'

    login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return token.key, None


def register_user(request):
    body = json.loads(request.body)
    username = body.get('username')
    email = body.get('email')
    senha = body.get('senha')

    if User.objects.filter(email=email).exists():
        return None, 'Email já cadastrado'

    user = User.objects.create_user(username=username, email=email, password=senha)
    login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return token.key, None


def logout_user(request):
    logout(request)
