# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect

from .models import Questoes, Historico

from .models import Classificacao

from .forms import QuestoesForm

from django.contrib.auth.models import Group

import pandas as pd

def checkGroupUsers(user):
	return user.groups.filter(name="Discentes").exists()


def checkGroupAdmin(user):
	return user.groups.filter(name="Administrador").exists()


@login_required
def home(request):
	return render(request, 'apps/home.html')
	
@login_required
@user_passes_test(checkGroupAdmin, login_url='http://127.0.0.1:8000/')

def inserir(request):
	if request.method == 'POST':
		form = QuestoesForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('http://127.0.0.1:8000')
	else:
		form = QuestoesForm()
		context = {
			'form': form,
		}
		return render(request, 'apps/inserir2.html', context)
		
@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def eixos(request):
	return render(request, 'apps/eixos.html')		

@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def humanas(request):
	return render(request, 'apps/humanas.html')	

@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def natureza (request):
	return render(request, 'apps/natureza.html')	

@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def linguagens (request):
	return render(request, 'apps/linguagens.html')	

@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def matematica (request):
	return render(request, 'apps/matematica.html')	



@login_required
@user_passes_test(checkGroupUsers, login_url='http://127.0.0.1:8000/')
def banco_de_questoes(request, cat):

	questoes = Questoes.objects.filter(classificacao=0)
	
	if request.method == "POST":

		for q in request.POST:
			if q != 'csrfmiddlewaretoken':
				resp = request.POST[q]
				quest = Questoes.objects.get(id=q)

				hist = Historico(questao=quest, id_user=request.user, resposta=resp, acerto=False)
				hist.save()

		return redirect('/')
	else:
		classificacao = Classificacao.objects.filter(categoria=cat)

		

		for i in classificacao:
			var = i.id 
			if i==0:
				questoes = Questoes.objects.filter(classificacao=var)
			else:
				q = Questoes.objects.filter(classificacao=var)
				def unir(questoes, q):
					return (questoes | q)

				questoes = unir(questoes, q)

	context = {
		'questoes': questoes,
	}
	
	return render(request, 'apps/banco.html', context)	

@login_required
def relatorio(request):

	hist = Historico.objects.filter(id_user=request.user).order_by('questao__classificacao')

	df_acertos = pd.DataFrame(columns=["gabarito", "resposta", "subcategoria", "acerto"])

	for h in hist: 
		acertou = int(h.questao.gabarito == h.resposta)
		df_acertos = df_acertos.append({
			"gabarito": h.questao.gabarito, 
			"resposta": h.resposta,
			"subcategoria": h.questao.classificacao.subcategoria,
			"acerto": acertou,
		}, ignore_index=True)

	total_sub = df_acertos[["subcategoria"]].value_counts()
	df_acertos = df_acertos.groupby(["subcategoria"]).sum("acerto").reset_index()
	
	print(df_acertos)

	context = {
		'df_acertos': df_acertos,
	}

	return render(request, 'apps/relatorio.html', context)

# Create your views here.
