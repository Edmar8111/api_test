# Generated by Django 5.0.6 on 2024-10-09 14:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_cont', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='id_livro',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]