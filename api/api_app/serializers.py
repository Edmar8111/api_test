import serializers
from api_app.models import FundoImobiliario

class FundoImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliario
        fields=[
            'id',
            'codigo',
            'setor',
            'dividend_yield_medio_12m',
            'vacancia_fisica',
            'quantidade_ativos'
        ]