from rest_framework import serializers,fields
from .models import Inicio,Perfil


#class InicioSerializers(serializers.ModelSerializer):
    #class Meta:
        #model= Inicio
        #fields = ['id','imagen','descripcion','fecha','autor']

class PerfilSerializers(serializers.ModelSerializer):

    def obtener_datos(self):
        fields = super(PerfilSerializer, self).get_fields()
        fields['imagen'] = PerfilSerializer(many=True)
        return fields

    class Meta:
        model= Perfil
        fields = ['imagenPerfil','nombre','infoCuenta','autor','imagen']