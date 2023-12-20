from django.db import models


class Conta(models.Model):
    matricula = models.CharField(max_length=64, unique=True, null=False) 
    saldo = models.FloatField(default=0, null=False)
class Chave(models.Model): 
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE) 
    descrição = models.CharField(max_length=64, unique=True, null=False)