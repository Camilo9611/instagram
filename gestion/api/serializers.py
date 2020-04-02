from rest_framework.serializers import ModelSerializer
from gestion.models import Inicio, Publicaciones, Perfil


class InicioListSerializer(ModelSerializer):
    class Meta:
        model= Inicio
        fields = ['id','imagen','descripcion','fecha','autor']

class InicioDetailSerializer(ModelSerializer):
    class Meta:
        model= Inicio
        fields = ['id','imagen','descripcion','fecha','autor']

class InicioUpdateSerializer(ModelSerializer):
    class Meta:
        model= Inicio
        fields = ['id','fecha','descripcion']


class InicioCreateSerializer(ModelSerializer):
    class Meta:
        model= Inicio
        fields = ['id','imagen','descripcion','fecha','autor']


################################################################################
##################   COMENTARIOS- LIKES ########################################

class PublicacionesListSerializer(ModelSerializer):
    class Meta:
        model= Publicaciones
        fields = ['id','imagen','comentarios','likes']

class PublicacionesDetailSerializer(ModelSerializer):
    class Meta:
        model= Publicaciones
        fields = ['id','imagen','comentarios','likes']

class PublicacionesUpdateSerializer(ModelSerializer):
    class Meta:
        model= Publicaciones
        fields = ['id','fecha','comentarios']

class PublicacionesCreateSerializer(ModelSerializer):
    class Meta:
        model= Publicaciones
        fields = ['id','imagen','comentarios','likes']


################################################################################
##################   PERFIL ########################################

class PerfilListSerializer(ModelSerializer):
    class Meta:
        model= Perfil
        fields = ['id','nombre','imagenPerfil','infoCuenta']

class PerfilDetailSerializer(ModelSerializer):
    class Meta:
        model= Perfil
        fields = ['id','nombre','imagenPerfil','infoCuenta']

    
class PerfilUpdateSerializer(ModelSerializer):
    class Meta:
        model= Perfil
        fields = ['id','nombre','imagenPerfil','infoCuenta']

