from django.http import HttpResponse as ht 
from django.shortcuts import render

def pag_perfil(request):
    #return ht("Pagina de perfil de Instagram")
    return render(request,'plantilla_perfil.html')
