from django.db import models
from datetime import datetime
from django.contrib import admin


# Create your models here.

class Presenca(models.Model):
    nomealuno = models.CharField(max_length=80)
    nomeprofessor = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural='Atividades'
        verbose_name='Atividade'
        

