from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('inserir/', views.inserir, name='inserir'),
    path('banco_de_questoes/<str:cat>/', views.banco_de_questoes, name='responder'),
    path('eixos/', views.eixos, name='eixos'),
    path('humanas/', views.humanas, name='humanas'),
    path('natureza/', views.natureza, name='natureza'),
    path('linguagens/', views.linguagens, name='linguagens'),
    path('matematica/', views.matematica, name='matematica'),
    path('relatorio/', views.relatorio, name='relatorio'),
]