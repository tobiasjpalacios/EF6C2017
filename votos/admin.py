# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *  
from django.contrib import admin

# TODO Register your models here.
admin.site.register(Candidato)
admin.site.register(Distrito)
admin.site.register(Votos)

