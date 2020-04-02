from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,CreateAPIView
from gestion.models import Inicio, Publicaciones, Perfil
from .serializers import InicioListSerializer,InicioDetailSerializer,InicioUpdateSerializer,InicioCreateSerializer
from .serializers import PublicacionesListSerializer,PublicacionesDetailSerializer,PublicacionesUpdateSerializer,PublicacionesCreateSerializer
from .serializers import PerfilListSerializer,PerfilDetailSerializer,PerfilUpdateSerializer

class InicioDetailAPIView(RetrieveAPIView):
    queryset= Inicio.objects.all()
    serializer_class= InicioDetailSerializer

class InicioUpdateAPIView(UpdateAPIView):
    queryset= Inicio.objects.all()
    serializer_class= InicioUpdateSerializer

class InicioDeleteAPIView(DestroyAPIView):
    queryset= Inicio.objects.all()
    serializer_class= InicioDetailSerializer

class InicioListAPIView(ListAPIView):
    queryset= Inicio.objects.all()
    serializer_class= InicioListSerializer
    lookup_field= 'pk'

class InicioCreateAPIView(CreateAPIView):
    queryset= Inicio.objects.all()
    serializer_class= InicioCreateSerializer

################################################################################
##################   COMENTARIOS- LIKES ########################################


class PublicacionesDetailAPIView(RetrieveAPIView):
    queryset= Publicaciones.objects.all()
    serializer_class= PublicacionesDetailSerializer

class PublicacionesUpdateAPIView(UpdateAPIView):
    queryset= Publicaciones.objects.all()
    serializer_class= PublicacionesUpdateSerializer

class PublicacionesDeleteAPIView(DestroyAPIView):
    queryset= Publicaciones.objects.all()
    serializer_class= PublicacionesDetailSerializer

class PublicacionesListAPIView(ListAPIView):
    queryset= Publicaciones.objects.all()
    serializer_class= PublicacionesListSerializer
    lookup_field= 'pk'

class PublicacionesCreateAPIView(CreateAPIView):
    queryset= Publicaciones.objects.all()
    serializer_class= PublicacionesCreateSerializer


################################################################################
##################   PERFIL ########################################

class PerfilDetailAPIView(RetrieveAPIView):
    queryset= Perfil.objects.all()
    serializer_class= PerfilDetailSerializer

class PerfilUpdateAPIView(UpdateAPIView):
    queryset=Perfil.objects.all()
    serializer_class= PerfilUpdateSerializer

class PerfilListAPIView(ListAPIView):
    queryset= Perfil.objects.all()
    serializer_class= PerfilListSerializer
    lookup_field= 'pk'
    