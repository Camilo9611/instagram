from django.urls import path, include,re_path
from .views import InicioListAPIView,InicioDetailAPIView,InicioUpdateAPIView,InicioDeleteAPIView,InicioCreateAPIView
from .views import PublicacionesListAPIView,PublicacionesDetailAPIView,PublicacionesUpdateAPIView,PublicacionesDeleteAPIView,PublicacionesCreateAPIView
from .views import PerfilListAPIView,PerfilDetailAPIView,PerfilUpdateAPIView

urlpatterns = [
    path('In/',InicioListAPIView.as_view(), name="listIn"),
    path('In/<int:pk>',InicioDeleteAPIView.as_view(), name="deleteIn"),
    path('In<int:pk>/',InicioDetailAPIView.as_view(), name="detailIn"),
    path('editarIn/<int:pk>/',InicioUpdateAPIView.as_view(), name="updateIn"),
    #path('eliminarIn/<int:pk>/',InicioDeleteAPIView.as_view(), name="deleteIn"),
    path('postearIn/',InicioCreateAPIView.as_view(), name="postearIn"),
    ##################################################################################
    path('Pu/',PublicacionesListAPIView.as_view(), name="listPu"),
    path('Pu/<int:pk>',PublicacionesDeleteAPIView.as_view(), name="deletePu"),
    path('Pu<int:pk>/',PublicacionesDetailAPIView.as_view(), name="detailPu"),
    path('editarPu/<int:pk>/',PublicacionesUpdateAPIView.as_view(), name="updatePu"),
    #path('eliminarPu/<int:pk>/',PublicacionesDeleteAPIView.as_view(), name="deletePu"),
    path('postearPu/',PublicacionesCreateAPIView.as_view(), name="postearPu"),
    ##################################################################################
    path('perfil/editarPer/',PerfilListAPIView.as_view(), name="listPer"),
    path('perfil/Per<int:pk>/',PerfilDetailAPIView.as_view(), name="detailPer"),
    path('perfil/editarPer/<int:pk>/',PerfilUpdateAPIView.as_view(), name="updatePer"),
    ]

