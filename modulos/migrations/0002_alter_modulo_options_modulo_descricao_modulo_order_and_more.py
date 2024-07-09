# Generated by Django 5.0.6 on 2024-07-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.TextField(default='Descrição padrão'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='modulo',
            name='publico',
            field=models.TextField(default='Público padrão'),
        ),
    ]