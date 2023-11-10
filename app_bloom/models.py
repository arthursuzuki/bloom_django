from django.db import models


# Create your models here.
class Crianca(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Feminino', 'Feminino'),
                                                      ('Masculino', 'Masculino'
                                                       ), ('Outro', 'Outro')])
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    historico_medico = models.FileField(upload_to='historicos/')
    autorizacao_responsavel = models.FileField(upload_to='autorizacoes/')

    def __str__(self):
        return self.nome
