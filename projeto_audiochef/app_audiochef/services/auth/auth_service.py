import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from app_audiochef.serializers import LoginSerializer, RegisterSerializer

logger = logging.getLogger(__name__)

def authenticate_user(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return None, "Corpo da requisição inválido"

    if 'senha' in body and 'password' not in body:
        body['password'] = body.pop('senha')

    serializer = LoginSerializer(data=body)
    if not serializer.is_valid():
        error_msg = next(iter(serializer.errors.values()))[0]
        return None, f"Erro: {error_msg}"

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    try:
        user_obj = User.objects.get(email=email)
    except User.DoesNotExist:
        logger.warning(f"Tentativa de login com email inexistente: {email}")
        return None, "Credenciais inválidas"

    user = authenticate(request, username=user_obj.username, password=password)
    if not user:
        logger.warning(f"Senha incorreta para o usuário: {email}")
        return None, "Credenciais inválidas"

    login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return token.key, None


def register_user(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return None, "Corpo da requisição inválido"
    if 'senha' in body and 'password' not in body:
        body['password'] = body.pop('senha')

    serializer = RegisterSerializer(data=body)
    if not serializer.is_valid():
        error_msg = next(iter(serializer.errors.values()))[0]
        return None, f"Erro: {error_msg}"

    data = serializer.validated_data
    
    if User.objects.filter(email=data['email']).exists():
        return None, "Este email já está cadastrado"
    
    if User.objects.filter(username=data['username']).exists():
        return None, "Este nome de usuário já está em uso"

    try:
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return token.key, None
    except Exception as e:
        logger.error(f"Erro fatal no registro: {str(e)}")
        return None, "Erro interno ao processar cadastro"


def logout_user(request):
    logout(request)
