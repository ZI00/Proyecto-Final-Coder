from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "ghola usuario/a"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludarfecha(request):
    hoy = datetime.now()
    saludo = f"hola usuraio, fecha:{hoy.day}/{hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


def inicio(request):
    contexto = {
        "profesor": "Pedro",
        "tutores": ["Mariano", "Ruben", "Luciano"],
        "comision": 55350,
    }
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response
