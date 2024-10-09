from rest_framework import viewsets
from api_cont.api_modulo import serializers
from api_cont import models
class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = models.Livros.objects.all()  