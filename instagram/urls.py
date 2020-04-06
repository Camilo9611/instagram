from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from gestion.views import PerfilViewSet


#router= DefaultRouter()
#router.register('gestion/api/publicar',InicioViewSet)
#router.register('gestion/api/editarperfil',PerfilViewSet)
#router.register('gestion/api/comentar',PublicacionesViewSet)


#urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cuentas.urls')),
    path('cuentas/',include('cuentas.urls')),
    path('gestion/',include('gestion.urls')),
    path('gestion/api/',include('gestion.api.urls')),
    path('',include('django.contrib.auth.urls')),
  
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
