from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from .services import recipe_service


# Create your views here.
def home(request):
    return render(request, 'app_audiochef/index.html')


class RecipesAPIView(APIView):
    def get(self, request):
        data = recipe_service.make_recipe()
        return Response(data, status=status.HTTP_200_OK)