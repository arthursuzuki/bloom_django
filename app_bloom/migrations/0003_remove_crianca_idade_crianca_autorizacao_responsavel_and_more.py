# Generated by Django 4.2 on 2023-11-27 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloom', '0002_feedbackpadrinho_padrinho_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crianca',
            name='idade',
        ),
        migrations.AddField(
            model_name='crianca',
            name='autorizacao_responsavel',
            field=models.FileField(default='static/arquives/PDF-teste.pdf', upload_to='autorizacoes/'),
        ),
        migrations.AddField(
            model_name='crianca',
            name='cpf',
            field=models.CharField(default=0, max_length=11),
        ),
        migrations.AddField(
            model_name='crianca',
            name='data_nascimento',
            field=models.DateField(default=0),
        ),
        migrations.AddField(
            model_name='crianca',
            name='endereco',
            field=models.CharField(default='r', max_length=100),
        ),
        migrations.AddField(
            model_name='crianca',
            name='genero',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='crianca',
            name='historico_medico',
            field=models.FileField(default='static/arquives/PDF-teste.pdf', upload_to='historicos/'),
        ),
        migrations.AddField(
            model_name='crianca',
            name='rg',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='nome',
            field=models.CharField(default='1', max_length=100),
        ),
    ]