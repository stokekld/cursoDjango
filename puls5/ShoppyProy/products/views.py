from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product

# Create your views here.
def hello_world(request):
	# return HttpResponse('hola mundo')
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))
