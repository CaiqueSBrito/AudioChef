from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'recipes', views.RecipesViewSet, basename='recipes')

urlpatterns = [
    path('api/recipes/', views.RecipesAPIView.as_view(), name='recipes'),
    path("", views.home, name="home"),
    path("login/", views.entrar, name="login"),
    path("registro/", views.registro, name="registro"),
    path("sair/", views.sair, name="sair"),
]