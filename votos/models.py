# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    
    
    
    """
    se decide utilizar este modelo para la clase Candidato porque es nesecesario el nombre 
    """
    nombre = models.CharField(max_length=50)
    
class Votos(models.Model):
    """
     se decide utilizar este modelo para la clase Votos candidato_votado para mas tarde tener una refenrencia  
     de cuantos votos son para cada candidato, y disctricto para mas tarde saber cuantos votaron en cada districto 
    votos null va a reflear la cantidad de votos null 
    """
    candidato = models.ForeignKey('Candidato',on_delete=models.CASCADE,)
    districto = models.ForeignKey('Distrito',on_delete=models.CASCADE,)
    votos_null =models.IntegerField('votos null',default=0)
    cantidad_votos = models.IntegerField('cantidad de votos',default=0)
    