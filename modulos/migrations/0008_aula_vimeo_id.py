# Generated by Django 5.0.6 on 2024-07-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
