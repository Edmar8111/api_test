from django.shortcuts import render
from rest_framework import generics
from .models import valores
from .serializers import valoresSerializer
# Create your views here.

class valores_api(generics.ListCreateAPIView):
    queryset = valores.objects.all()
    serializer_class = valoresSerializer
