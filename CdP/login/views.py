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
        
        conta = Conta.objects.filter(matricula=request.POST['matricula'])

        if conta.exists():
            c_matricula = conta[0].matricula
            request.session['c_matricula'] = c_matricula
            return redirect('transferencia')
        else:
            return render(request, 'login/index.html')
    else:
        return render(request, 'login/index.html')

def transf(request):
    c_matricula = request.session.get('c_matricula')
    l_conta = Conta.objects.filter(matricula=c_matricula)

    if request.method == "POST":
        chave = Chave.objects.filter(descrição=request.POST['chave-pix'])

        if chave.exists():
            conta = (chave[0]).conta
            conta = Conta.objects.filter(matricula=conta.matricula)
            
            if float(request.POST['dinheiro']) <= l_conta[0].saldo:

                conta.update(saldo=conta[0].saldo + float(request.POST['dinheiro']))
                l_conta.update(saldo=l_conta[0].saldo - float(request.POST['dinheiro']))
            
                return render(request, "login/transf.html")
            else:
                return render(request, "login/transf.html")
        else:
            return render(request, "login/transf.html")
    else:
        return render(request, "login/transf.html")