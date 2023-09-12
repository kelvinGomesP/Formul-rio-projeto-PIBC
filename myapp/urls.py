from django.urls import path
from . import views


urlpatterns = [
    
   path('', views.formulario, name='formularioidp'),
    path('sucesso/', views.pagina_de_sucesso, name='pagina_de_sucesso'),
    path('idp/', views.formulario, name='formulario')
]
