from django.db import models


# Create your models here.
class Crianca(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Feminino', 'Feminino'),
                                                      ('Masculino', 'Masculino'
                                                       ), ('Outro', 'Outro')])
    cpf = models.CharField(max_length=11,unique=True)
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    historico_medico = models.FileField(upload_to='historicos/')
    autorizacao_responsavel = models.FileField(upload_to='autorizacoes/')

    def __str__(self):
        return self.nome
    
class Recordacoes(models.Model):
    cpf = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    imagem_recordacao = models.ImageField(upload_to='recordacoes_imagens/')
    data = models.DateField(("Data"), auto_now=True, auto_now_add=False)

class Padrinho(models.Model):
    nome= models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=500)
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    rg = models.CharField(max_length=10)
    profissao = models.CharField(max_length=40)
    reason = models.CharField(max_length=1000)
    senha = models.CharField(max_length=20,default="12345678")

class Pirralho(models.Model):
    nome = models.CharField(max_length=100)
    idade =models.CharField(max_length=3)

class destinatarioFeedback(models.TextChoices):
    AFILHADO = "Afilhado"
    GOTAS = "Gotas de Flor"

class FeedbackPadrinho(models.Model):
    nome = models.CharField(max_length=100)
    destinatario = models.TextField(choices=destinatarioFeedback.choices)
    mensagem = models.CharField(max_length=1000)

class Atividades(models.Model):
    mes = models.CharField(max_length=255)
    atividade = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    avaliacao_red = models.IntegerField()
    avaliacao_yellow = models.IntegerField()
    avaliacao_green = models.IntegerField()

    def _str_(self):
        return f"{self.mes} - {self.atividade} - Atividades Realizadas"