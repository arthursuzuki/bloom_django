from django.db import models


# Create your models here.


class Padrinho(models.Model):
    nome= models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=500)
    cpf = models.CharField(max_length=12,unique=True)
    email = models.EmailField(max_length=254)
    rg = models.CharField(max_length=10)
    profissao = models.CharField(max_length=40)
    reason = models.CharField(max_length=1000)
    senha = models.CharField(max_length=20,default="12345678")

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
    foto = models.FileField(upload_to='fotocrianca/')
    naturalidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    identidade = models.CharField(max_length=20)
    dt_expedicao_ident = models.DateField()
    orgao_expeditor = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    cep = models.IntegerField()
    raca = models.CharField(max_length=50, choices=[('Preto', 'Preto'), ('Branca', 'Branca'), ('Parda', 'Parda'), ('Amarela', 'Amarela'),('Outra','Outra')])
    telefone_responsavel = models.IntegerField()



    def __str__(self):
        return self.nome
    
class Recordacoes(models.Model):
    cpf = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    imagem_recordacao = models.ImageField(upload_to='recordacoes_imagens/')
    data = models.DateField(("Data"), auto_now=True, auto_now_add=False)

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
    

class DadosCrianca(models.Model):
    mes = models.CharField(max_length=255)
    atividade = models.CharField(max_length=255)
    carga_horaria = models.CharField(max_length=255)
    desempenho = models.CharField(max_length=255)


from django.db import models

class ChildActivity(models.Model):
    MONTH_CHOICES = [
        ('janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('marco', 'Março'),
        ('abril', 'Abril'),
        ('maio', 'Maio'),
        ('junho', 'Junho'),
        ('julho', 'Julho'),
        ('agosto', 'Agosto'),
        ('setembro', 'Setembro'),
        ('outubro', 'Outubro'),
        ('novembro', 'Novembro'),
        ('dezembro', 'Dezembro'),
    ]

    ACTIVITY_CHOICES = [
        ('capoeira', 'Capoeira'),
        ('coral', 'Coral'),
        ('volei', 'Vôlei'),
        ('futebol', 'Futebol'),
        ('artes', 'Artes'),
        ('yoga', 'Yoga'),
        ('meioambiente', 'Meio Ambiente'),
        ('cidadania', 'Cidadania'),
    ]

    DESMPENHO_CHOICES = [
        ('otimo', 'Ótimo'),
        ('regular', 'Regular'),
        ('ruim', 'Ruim'),
    ]

    mes = models.CharField(max_length=20, choices=MONTH_CHOICES)
    atividade_secao1 = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    carga = models.CharField(max_length=50)
    desempenho_secao1 = models.CharField(max_length=20, choices=DESMPENHO_CHOICES)
    crianca = models.ForeignKey(Crianca,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mes} - {self.atividade_secao1}'
