from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse    

def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        if usuario == "" or senha == "":
            messages.error(request, "Campos usuario e senha nao pode ser vazio.")
            return redirect('login')
        
        usuario_logado = auth.authenticate(request, username=usuario, password=senha)
        if usuario_logado is not None:
            auth.login(request, usuario_logado)
            messages.success(request, 'Login realizado com sucesso')
            return redirect ('inicio')
        else:
            messages.error(request, "Login ou senha incorreto.")
            return redirect ('login')

    return render(request, 'login.html')

def inicio(request):
    return render(request, 'template.html')

def sair(request):
    auth.logout(request)
    return  redirect('login')
    
