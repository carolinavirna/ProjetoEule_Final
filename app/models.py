# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import get_user_model

class Classificacao(models.Model):

	eixo = models.CharField(max_length=100)
	categoria = models.CharField(max_length=100)
	subcategoria = models.CharField(max_length=100)

	def __str__(self):
		return (self.subcategoria+' - '+ self.categoria+' - '+self.eixo)

class Questoes(models.Model):

	STATUS = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
	)

	enunciado = models.TextField()
	itemA = models.TextField()
	itemB = models.TextField()
	itemC = models.TextField()
	itemD = models.TextField()
	itemE = models.TextField()
	gabarito = models.CharField(
		max_length=1,
		choices = STATUS,
	)
	classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)

class Historico(models.Model):

	questao = models.ForeignKey(Questoes, on_delete=models.CASCADE)
	id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	resposta = models.CharField(max_length=1)
	acerto = models.CharField(max_length=1)

# Create your models here.
