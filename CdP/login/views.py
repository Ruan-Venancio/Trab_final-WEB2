from django.shortcuts import render, redirect
from .models import Conta, Chave

quant_registros = Conta.objects.count()

def casdastrar(request):

    conta_criada = Conta(matricula=request.POST['matricula'], 
                        saldo=request.POST['saldo'])
    conta_criada.save()

    chave_criada = Chave(conta=conta_criada, 
                        descrição=request.POST['chave-pix'])
    chave_criada.save()

    return render(request, "login/tel_cad.html")

def index(request):

    matricula = Conta.objects.filter(matricula=request.POST['matricula'])

    if matricula.exists():
        return redirect('transferencia')
    else:
        return render(request, 'login/index.html')

def transf(request):
    ...