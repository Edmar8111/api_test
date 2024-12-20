# Generated by Django 5.1 on 2024-10-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(default='desconhecida', max_length=100)),
                ('sigla_estado', models.CharField(default='desconhecida', max_length=100)),
                ('data_previsao', models.DateTimeField(auto_now=True)),
                ('maxima', models.IntegerField(default=0)),
                ('minima', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'valores',
            },
        ),
    ]
