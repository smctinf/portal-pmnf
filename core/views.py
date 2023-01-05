from django.shortcuts import render
from .models import Servico
from django.db.models import Count

# Create your views here.
def index(request):
    servicos=Servico.objects.all().order_by('nome')
    secretarias=[]
    for item in servicos.values('secretaria').annotate(dcount=Count('secretaria')).order_by():
        secretarias.append([item['secretaria'],[servicos.filter(secretaria=item['secretaria'])]])
    print(secretarias)
    context={
        'titulo': 'PORTAL DO CIDADÃO',
        'carousel': False,
        'servicos': servicos,
        'secretarias': secretarias
    }
    return render(request, 'index.html', context)

def index2(request):
    servicos=Servico.objects.all().order_by('nome')
    secretarias=[]
    for item in servicos.values('secretaria').annotate(dcount=Count('secretaria')).order_by():
        secretarias.append([item['secretaria'],[servicos.filter(secretaria=item['secretaria'])]])
    print(secretarias)
    context={
        'titulo': 'PORTAL DO CIDADÃO',
        'carousel': True,
        'servicos': servicos,
        'secretarias': secretarias
    }
    return render(request, 'index.html', context)