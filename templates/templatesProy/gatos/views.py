from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Gato

def gato(request):
	gatos = Gato.objects.order_by('id')
	template = loader.get_template('gato.html')
	title = 'los gatos son cool'
	context = {
		'gatos': gatos,
		'title': title
	}
	return HttpResponse(template.render(context, request))

def saludo(request):
	template = loader.get_template('saludo.html')
	big_title = 'Encabezado de la pagina'
	title = 'saludo gato'

	context = {
		'big_title': big_title,
		'title': title
	}
	return HttpResponse(template.render(context, request))