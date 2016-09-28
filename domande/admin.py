from django.contrib import admin
from .models import Domanda
from .models import Risposta
from .models import Annuncio

admin.site.register(Domanda)
admin.site.register(Risposta)
admin.site.register(Annuncio)
