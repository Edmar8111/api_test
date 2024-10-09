# Generated by Django 5.0.6 on 2024-10-09 13:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano_lan', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=255)),
                ('criado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
