import requests
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from . import serializers

# Create your views here.
def home (request):
    return render(request, 'app_audiochef/index.html')
