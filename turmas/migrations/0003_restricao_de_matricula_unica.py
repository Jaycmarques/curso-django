# Generated by Django 5.0.7 on 2024-07-24 01:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0002_matricula_turma_alunos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['turma', 'data']},
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('usuario', 'turma')},
        ),
    ]
