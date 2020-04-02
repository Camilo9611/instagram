from django.urls import path, include
from cuentas.views import registro, login_sesion, logout_sesion

app_name='cuentas'

urlpatterns = [
    path('registro/',registro,name="registro" ),
    path('login_sesion/',login_sesion,name="login"),
    path('',login_sesion,name="login"),
    path('logout/cuentas/',logout_sesion, name="logout"),
    #path('accounts/',include('django.contrib.auth.urls')),

    
]