# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI    
    candidato = Candidato.objects.all()
    votosnull= Votos.objects.filter(candidato__isnull=True)
    context['allvotos'] = Votos.objects.all()
    context['votosnull'] =Votos.objects.filter(candidato__isnull=True
    allvotos =  Votos.objects.all()                                )
    #porcentajevotosnull = int(votosnull)*100)/int(candidatos)
   
    contador = {}
    for voto in allvotos:
        contador=contador+1  
    print contador
    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}

    #TODO TU CODIGO AQUI

    return render(request,'distrital.html',context)
