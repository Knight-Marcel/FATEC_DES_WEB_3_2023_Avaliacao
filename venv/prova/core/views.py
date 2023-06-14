from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import datetime
from django.shortcuts import redirect
from .models import Presenca 
from django import forms
from django.forms import ModelForm







#função para consultar
def index(request):
    lista = []
    presencas = Presenca.objects.all()
    
    for presenca in presencas:
        item = {
            'nomealuno': presenca.nomealuno,
            'nomeprofessor': presenca.nomeprofessor
        }
        lista.append(item)
            
    context = {'lista': lista}
    return render(request, 'index.html', context)




#função para cadastrar atividade
class PresencaForm(ModelForm):
    class Meta:
        model = Presenca
        fields = ['nomealuno', 'nomeprofessor']

def cadastro(request):
    if request.method == 'POST':

        form = PresencaForm(request.POST)


        if form.is_valid():
            nomealuno = form.cleaned_data['nomealuno']
            nomeprofessor = form.cleaned_data['nomeprofessor']


            form.save()
            
            return index(request)
                 
        return HttpResponse('Erro de cadastro')
    else:

        contexto = {'form': Presenca() }    
        return render(request,'cadastro.html', contexto)

from django.shortcuts import get_object_or_404, redirect


    
