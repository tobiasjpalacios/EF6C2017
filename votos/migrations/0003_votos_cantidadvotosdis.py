# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0002_remove_candidato_cantidad_votosel'),
    ]

    operations = [
        migrations.AddField(
            model_name='votos',
            name='cantidadvotosdis',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='votos.Distrito'),
            preserve_default=False,
        ),
    ]
