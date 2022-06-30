from django import forms
from .models import Questoes 

class QuestoesForm(forms.ModelForm):

	class Meta:
		model = Questoes
		fields = ('enunciado', 'itemA', 'itemB', 'itemC', 'itemD', 'itemE', 'gabarito', 'classificacao')
