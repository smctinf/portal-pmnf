from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'titulo': 'PORTAL DE SERVIÇOS ONLINE'
    }
    return render(request, 'index.html', context)