from django.shortcuts import render, redirect
from .models import Conta, Chave

quant_registros = Conta.objects.count()

def casdastrar(request):
    if request.method == "POST":
        conta_criada = Conta(matricula=request.POST['matricula'], 
                            saldo=50)
        conta_criada.save()

        chave_criada = Chave(conta=conta_criada, 
                            descrição=request.POST['chave-pix'])
        chave_criada.save()
        
        return redirect('transferencia')
    else:
        return render(request, "login/tel_cad.html")
    
def index(request):
    if request.method == "POST":
        
        matricula = Conta.objects.filter(matricula=request.POST['matricula'])

        if matricula.exists():
            saldo = matricula[0].saldo
            return redirect('transferencia', saldo=saldo)
        else:
            return render(request, 'login/index.html')
    else:
        return render(request, 'login/index.html')

def transf(request, saldo):
    print(saldo)
    if request.method == "POST":
        chave = Chave.objects.filter(decrição=request.POST['chave-pix'])

        if chave.exists():
            conta = (chave[0]).conta
            conta.update(saldo=conta.saldo + request.POST['dinheiro'])
        else:
            return render(request, "login/transf.html")
    else:
        return render(request, "login/transf.html")