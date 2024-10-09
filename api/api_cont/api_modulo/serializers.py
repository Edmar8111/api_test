from rest_framework import serializers
from api_cont import models

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livros
        fields = '__all__'