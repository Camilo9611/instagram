from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as uc
from django.contrib.auth.forms import AuthenticationForm as au
from gestion.views import historias
from django.contrib.auth import login,logout


# Create your views here.

def registro(request):
    if request.method == 'POST':
        form=uc(request.POST)
        if form.is_valid():
            user=form.save() #Autamaticar retorna los valores
            login(request,user)
            return redirect('gestion:crearP')
    else:    
        form = uc()
    return render(request,'cuentas/plantilla_registro.html',{'form':form})

def login_sesion(request):
    if request.method =='POST':
        form =au(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('gestion:list')
    else:
        form= au()
    return render(request,'cuentas/plantilla_login.html',{'form':form})


def logout_sesion(request):
    #if request.method=='GET':
    return redirect ("cuentas:login")
            