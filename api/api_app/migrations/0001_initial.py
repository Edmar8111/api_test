# Generated by Django 5.1 on 2024-10-08 20:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundoImobiliario',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8)),
                ('setor', models.CharField(choices=[('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido', 'Híbrido'), ('lajes_corporativas', 'Lajes Corporativas'), ('logistica', 'Logística'), ('residencial', 'Residencial'), ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')], max_length=30)),
                ('dividend_yield_medio_12m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacancia_financeira', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacancia_fisica', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade_ativos', models.IntegerField(default=0)),
            ],
        ),
    ]