from .services import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, basename='recipes')

urlpatterns = [
    path('api/recipes/random/', views.RecipeRandomAPIView.as_view(), name='recipes_random'),
    path('api/recipes/search/', views.RecipeSearchAPIView.as_view(), name='recipes_search'),
    path('api/recipes/detail/', views.RecipeDetailAPIView.as_view(), name='recipes_detail'),
    path("", views.home, name="home"),
    path("buscar/", views.search_page, name="search_page"),
    path("crud/", views.crud_page, name="crud_page"),
    path("login/", views.entrar, name="login"),
    path("registro/", views.registro, name="registro"),
    path("sair/", views.sair, name="sair"),
    path("api/", include(router.urls))
]