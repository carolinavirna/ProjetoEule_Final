from django.shortcuts import render, reverse

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect

from django.views import generic

from .forms import CustomUserCreationForm

from django.contrib.auth.models import Group


def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			g_discente = Group.objects.get(name= "Discentes")
			new_user.groups.add(g_discente)
			new_user.save()
		return HttpResponseRedirect('/accounts/login/')
	else:
		form = CustomUserCreationForm()
	
	context = {
		'form': form,
	}

	return render(request, 'registration/register.html', context)

def registeradmin(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			g_admin = Group.objects.get(name= "Administrador")
			new_user.groups.add(g_admin)
			new_user.save()
		return HttpResponseRedirect('/accounts/login/')
	else:
		form = CustomUserCreationForm()
	
	context = {
		'form': form,
	}

	return render(request, 'registration/registeradmin.html', context)



# Create your views here.
