# Generated by Django 4.2 on 2023-11-30 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloom', '0006_atividades'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosCrianca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=255)),
                ('atividade', models.CharField(max_length=255)),
                ('carga_horaria', models.CharField(max_length=255)),
                ('desempenho', models.CharField(max_length=255)),
            ],
        ),
    ]