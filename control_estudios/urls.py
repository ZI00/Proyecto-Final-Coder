from django.urls import path

from control_estudios.views import listar_estudiantes

#Estas son las URLS de la app control estudios
urlpatterns = [
    path("estudiantes/", listar_estudiantes),
]