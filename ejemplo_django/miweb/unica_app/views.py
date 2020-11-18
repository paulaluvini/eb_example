from django.shortcuts import render
from django.http import HttpResponse

import random

from unica_app.models import NumeroHistorico


def numero_al_azar_decimal(request):
	# Creo el numero al azar y lo guardo en el contexto
	numero = random.random()

	# Obtengo informacion del browser porque la queria
	# guardar 
	browser_information = request.META['HTTP_USER_AGENT']

	# Creo un objeto de mis modelos para persistir
	# este numero
	nh = NumeroHistorico.objects.create(number=numero,
		request_information = browser_information,
		ip = request.META['REMOTE_ADDR'],
		port = request.META['SERVER_PORT'])

	# guardo en una variable los NumeroHistorico que
	# ya salieron previamente
	numeros_historicos = NumeroHistorico.objects.all()
	# numeros_historicos = NumeroHistorico.objects.filter(request_information='python-requests/2.23.0')
	context = {'numero_variable':nh, 
	'lista_numeros_historicos':numeros_historicos}


	return render(request, 'numeros_lindos.html', context)

def numero_al_azar_entero_en_rango(request,param1,param2):
	num = random.randint(param1,param2)
	context = {'numero_variable':num}
	return render(request, 'numeros_lindos.html', context)

