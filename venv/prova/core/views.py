from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import datetime
from django.shortcuts import redirect

data = datetime.date.today()

#função para consultar
def index(request):
    lista=[]
    context={'lista':lista}
    lista=Presenca.objects.all()
    
    for item in lista:
        if item.data == data:
            context['lista'].append(item)
            
    return render(request,'index.html', context)


#função para cadastrar atividade
def cadastro(request):
    if request.method == 'POST':

        form = Presenca(request.POST)

        if form.is_valid():
            nomealuno=form.data['nome']
            nomeaprofessor=form.data['nome']

            form.save()
            return index(request)
        return HttpResponse('Erro de cadastro')
    else:

        contexto = {'form': Presenca() }    
        return render(request,'index.html', contexto)

from django.shortcuts import get_object_or_404, redirect


    
