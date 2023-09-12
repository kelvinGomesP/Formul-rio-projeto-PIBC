from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.

"""
class Responsavel(models.Model):
        
    FAIXAS_SALARIAIS = (
        ('Até R$ 1.000', 'Até R$ 1.000'),
        ('R$ 1.001 a R$ 3.000', 'R$ 1.001 a R$ 3.000'),
        ('R$ 3.001 a R$ 5.000', 'R$ 3.001 a R$ 5.000'),
        ('R$ 5.001 a R$ 7.000', 'R$ 5.001 a R$ 7.000'),
        ('R$ 7.001 a R$ 10.000', 'R$ 7.001 a R$ 10.000'),
        ('R$ 10.001 a R$ 15.000', 'R$ 10.001 a R$ 15.000'),
        ('Acima de R$ 15.001', 'Acima de R$ 15.001'),
    )

    ESCOLARIDADE_CHOICES = [
        ('Fundamental', 'Ensino Fundamental'),
        ('Medio', 'Ensino Médio'),
        ('Superior', 'Ensino Superior'),
        ('PosGraduacao', 'Pós-Graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    
    ]

    Range_salarial = models.CharField(max_length=255, choices=FAIXAS_SALARIAIS, blank=True, null=True)
    Escolaridade = models.CharField(max_length=255, choices=ESCOLARIDADE_CHOICES, blank=True, null=True)



class Aluno(models.Model):
    Autorizo = models.BooleanField(default=False)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    RACA_CHOICES = [
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('PARDO', 'Pardo'),
        ('INDIGENA', 'Indígena'),
        ('AMARELO', 'Amarelo'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('SOLTEIRO', 'Solteiro(a)'),
        ('CASADO', 'Casado(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
        ('VIUVO', 'Viúvo(a)'),
        ('UNIAO_ESTAVEL', 'União Estável'),
    ]
    
    FAIXAS_SALARIAIS = (
        ('Até R$ 1.000', 'Até R$ 1.000'),
        ('R$ 1.001 a R$ 3.000', 'R$ 1.001 a R$ 3.000'),
        ('R$ 3.001 a R$ 5.000', 'R$ 3.001 a R$ 5.000'),
        ('R$ 5.001 a R$ 7.000', 'R$ 5.001 a R$ 7.000'),
        ('R$ 7.001 a R$ 10.000', 'R$ 7.001 a R$ 10.000'),
        ('R$ 10.001 a R$ 15.000', 'R$ 10.001 a R$ 15.000'),
        ('Acima de R$ 15.001', 'Acima de R$ 15.001'),
    )


    TRABALHA_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    
    Nome = models.CharField(max_length=100)
    Matrícula = models.IntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(1000000),
            MaxValueValidator(9999999),
        ]
    )
   
    Responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, null=True, blank=True)
    
    Sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    #Data_Nascimento = models.DateField(null=True, blank=True)#default=datetime(2000, 1, 1)

    Renda_Própria = models.CharField(max_length=25, choices=FAIXAS_SALARIAIS, default='0')
    Mora_Com_Pais = models.BooleanField(default=False)
    Trabalha = models.CharField(max_length=3, choices=TRABALHA_CHOICES, default='Não')
    Quantidade_Filhos = models.IntegerField(default=0)
    Raca = models.CharField(max_length=20, choices=RACA_CHOICES, default='BRANCO')
    Estado_Civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, default='Solteiro')


 #default=1)
 
 """
 
 
class Aluno(models.Model):
    Autorizo = models.BooleanField(default=False)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    RACA_CHOICES = [
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('PARDO', 'Pardo'),
        ('INDIGENA', 'Indígena'),
        ('AMARELO', 'Amarelo'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('SOLTEIRO', 'Solteiro(a)'),
        ('CASADO', 'Casado(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
        ('VIUVO', 'Viúvo(a)'),
        ('UNIAO_ESTAVEL', 'União Estável'),
    ]

    FAIXAS_SALARIAIS = (
        ('Até R$ 1.000', 'Até R$ 1.000'),
        ('R$ 1.001 a R$ 3.000', 'R$ 1.001 a R$ 3.000'),
        ('R$ 3.001 a R$ 5.000', 'R$ 3.001 a R$ 5.000'),
        ('R$ 5.001 a R$ 7.000', 'R$ 5.001 a R$ 7.000'),
        ('R$ 7.001 a R$ 10.000', 'R$ 7.001 a R$ 10.000'),
        ('R$ 10.001 a R$ 15.000', 'R$ 10.001 a R$ 15.000'),
        ('Acima de R$ 15.001', 'Acima de R$ 15.001'),
    )

    TRABALHA_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    ESCOLARIDADE_CHOICES = [
        ('Fundamental', 'Ensino Fundamental'),
        ('Medio', 'Ensino Médio'),
        ('Superior', 'Ensino Superior'),
        ('PosGraduacao', 'Pós-Graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    ]

    Nome = models.CharField(max_length=100)
    Matrícula = models.IntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(1000000),
            MaxValueValidator(9999999),
        ]
    )

    

    Sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    Renda_Própria = models.CharField(max_length=25, choices=FAIXAS_SALARIAIS, default='0')
    Mora_Com_Pais = models.BooleanField(default=False)
    Trabalha = models.CharField(max_length=3, choices=TRABALHA_CHOICES, default='Não')
    Quantidade_Filhos = models.IntegerField(default=0)
    Raca = models.CharField(max_length=20, choices=RACA_CHOICES, default='BRANCO')
    Estado_Civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, default='Solteiro')
    Range_salarial = models.CharField(max_length=255, choices=FAIXAS_SALARIAIS, blank=True, null=True)
    Escolaridade = models.CharField(max_length=255, choices=ESCOLARIDADE_CHOICES, blank=True, null=True)