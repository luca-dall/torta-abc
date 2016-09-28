from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import date
from reportlab.pdfgen import canvas

from .models import Domanda, Risposta, Annuncio
# Create your views here.

def index(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login'))

	domande = Domanda.objects.order_by('id')
	risposte = Risposta.objects.filter(utente = request.user, anno = date.today().year).order_by('domanda')
	annuncio = Annuncio.objects.get(utente = request.user, anno = date.today().year)

	context = {'domande': domande, 'risposte': risposte, 'annuncio':annuncio}
	return render(request, 'domande/index.html', context)

def save(request):
	user = User.objects.get(id = int(request.POST.get('user', False)))
	year = request.POST.get('year', False)
	question = Domanda.objects.get(id = int(request.POST.get('question', False)))
	response = request.POST.get('response', False)
	try:
		entry = Risposta.objects.get(utente = user, anno = year, domanda = question)
	except Risposta.DoesNotExist:
		entry = None
	
	if entry == None:
		new_entry = Risposta(utente=user, anno=year, domanda=question, risposta=response)
		new_entry.save()
	else:
		entry.risposta = response
		entry.save()		

	return HttpResponse(status=201)

def announce(request):
	user = User.objects.get(id = int(request.POST.get('user', False)))
	year = request.POST.get('year', False)
	status = request.POST.get('status', False)

	if status == 'false':
		status = False
	elif status == 'true':
		status = True

	try:
		entry = Annuncio.objects.get(utente = user, anno = year)
	except Annuncio.DoesNotExist:
		entry = None
	
	if entry == None:
		entry = Annuncio(utente = user, anno = year, stato = status)
		entry.save()		
	else:
		entry.stato = status
		entry.save()

	return HttpResponse(status=201)


def exportpdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="torta-ABC.pdf"'

	p = canvas.Canvas(response)
	p.drawString(100, 100, "Hello world.")

	p.showPage()
	p.save()
	return response