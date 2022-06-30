# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Questoes
from .models import Classificacao
from .models import Historico


admin.site.register(Questoes)
admin.site.register(Classificacao)
admin.site.register(Historico)


# Register your models here.
