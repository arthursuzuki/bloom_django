# Generated by Django 4.2 on 2023-11-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloom', '0002_crianca_padrinho_pirralho_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='padrinho',
            name='senha',
            field=models.CharField(default='12345678', max_length=20),
        ),
    ]