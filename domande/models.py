# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime


YEAR_CHOICES = [(r, r) for r in range(2016, datetime.date.today().year+1)]

class Domanda(models.Model):
    fetta = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C')])
    categoria = models.CharField(max_length=200)
    sotto_categoria = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return str(self.id).encode('utf8') + '.' + self.fetta.encode('utf8') + ' - ' + self.text.encode('utf8')

    def safe_categoria(self):
        categoria = self.categoria.replace(' ', '_')
        return categoria.encode('utf8').replace('°','')

class Risposta(models.Model):
    utente = models.ForeignKey(User, unique=False)
    anno = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    domanda = models.ForeignKey(Domanda)
    risposta = models.BooleanField(default=False)

class Annuncio(models.Model):
    utente = models.ForeignKey(User, unique=False)
    anno = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    stato = models.BooleanField(default=False)
