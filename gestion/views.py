from django.shortcuts import render, redirect
from gestion.models import Inicio,Perfil, Publicaciones
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PerfilSerializers
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from gestion.forms import PerfilForm

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class= PerfilSerializers
    queryset = Perfil.objects.all()

@login_required
def historias(request):
    posters= Inicio.objects.all().order_by('fecha')
    posters2= Publicaciones.objects.all()
    

    datos=[]
    for i in posters:
        var= i.id
        for j in posters2:
            var2=j.imagen_id
            if var==var2:
                var3=j.comentarios
                datos.append(dict([(var2,var3)]))
                print (datos)

    datoslikes=[]
    for i in posters:
        var= i.id
        for j in posters2:
            var2=j.imagen_id
            if var==var2:
                lik= Publicaciones.objects.filter(imagen_id=var).count()
                                                                #.aggregate(Sum('likes'))
                datoslikes.append(dict([(var2,lik)]))
                break   

                     
    context= {
        'posters':posters,
        'posters2':posters2,
        'datos': datos,
        'datoslikes': datoslikes,
    }

    return render(request,'gestion/historias_inicio.html',context)

@login_required    
def perfil(request):
    posters= Perfil.objects.all().order_by('-id')
    posters3=User.objects.order_by('-last_login').first()

    objeto1= Inicio.objects.all().order_by('fecha')

    for i in posters:
        var= i.autor
        if var == posters3:
            var5=i.autor_id
            posters4=Perfil.objects.all().filter(autor_id =var5)



    datos=[]
    for i in objeto1:
        var20= i.autor
        if var20==posters3:
            var30=i.imagen
            datos.append(dict([(var20,var30)]))

        print(datos)

    context= {
        'posters':posters,
        'posters3':posters3,
        'posters4':posters4,
        'datos': datos,

    }            
    return render(request,'gestion/plantilla_perfil.html',context)

        
def crear_perfil(request):
    form = PerfilForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form= PerfilForm()
        return redirect('gestion:list')

    context = {
        'form': form
    }
    return render(request,'gestion/crear_perfil.html', context)


def Funcion_edit(request):
    return redirect('/gestion/api/perfil/editarPer/')


