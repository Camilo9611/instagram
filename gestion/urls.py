from django.urls import path, include
from gestion.views import historias,perfil, crear_perfil
from gestion.api.views import PerfilListAPIView,PerfilDetailAPIView,PerfilUpdateAPIView

app_name='gestion'

urlpatterns = [
    path('',historias, name="list"),
    path('perfil/',perfil, name="perfil"),
    path('crearPerfil/',crear_perfil, name="crearP"),
    path('api/perfil/editarPer/<int:pk>/',PerfilUpdateAPIView.as_view(), name="updatePer"),
    #path('accounts/',include('django.contrib.auth.urls')),
    ]

