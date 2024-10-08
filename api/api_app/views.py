from django.shortcuts import render

# Create your views here.
from api_app.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from api_app.models import FundoImobiliario


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset=FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permissions_classes = [permissions.IsAuthenticated]
