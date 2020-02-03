from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .forms import  AddFormMusico, AddFormGrupo
from .models import *
import json
# Create your views here. 

def index(request):
	if request.user.is_authenticated:
		return render(request, 'base.html', {'username':request.user.username})
	return render(request, 'base.html')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def AddMusico(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = AddFormMusico(request.POST)
			if form.is_valid():
				form.save()
			return redirect('index')
		else:
			form = AddFormMusico()
		return render(request, 'musico.html', {'form':form, 'username':request.user.username})
	return render(request, 'base.html')
    

def ModifyMusico(request, id_musico):
	if request.user.is_authenticated:
		musico = Musico.objects.get(id=id_musico)
		if request.method == 'GET':
			form = AddFormMusico(instance=musico)
		else:
			form = AddFormMusico(request.POST, instance=musico)
			if form.is_valid():
				form.save()
			return redirect('listar_musico')
		return render(request, 'musico.html', {'form':form, 'username':request.user.username})
	return render(request, 'base.html')

def DeleteMusico(request, id_musico):
	if request.user.is_authenticated:
		musico = Musico.objects.get(id=id_musico)
		if request.method == 'POST':
			musico.delete()
			return redirect('listar_musico')
		return render(request, 'delete.html', {'variable':musico, 'username':request.user.username})
	return render(request, 'base.html')

def ListMusico(request):
	if request.user.is_authenticated:
		musico = Musico.objects.all()
		contexto = {'musicos':musico, 'username':request.user.username}
		return render(request, 'listar_musicos.html', contexto)
	return render(request, 'base.html')

def AddGrupo(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = AddFormGrupo(request.POST)
			if form.is_valid():
				form.save()
			return redirect('index')
		else:
			form = AddFormGrupo()
		return render(request, 'grupo.html', {'form':form, 'username':request.user.username})
	return render(request, 'base.html')
    

def ModifyGrupo(request, id_grupo):
	if request.user.is_authenticated:
		grupo = Grupo.objects.get(id=id_grupo)
		if request.method == 'GET':
			form = AddFormGrupo(instance=grupo)
		else:
			form = AddFormGrupo(request.POST, instance=grupo)
			if form.is_valid():
				form.save()
			return redirect('listar_grupo')
		return render(request, 'grupo.html', {'form':form, 'username':request.user.username})
	return render(request, 'base.html')

def DeleteGrupo(request, id_grupo):
	if request.user.is_authenticated:
		grupo = Grupo.objects.get(id=id_grupo)
		if request.method == 'POST':
			grupo.delete()
			return redirect('listar_grupo')
		return render(request, 'delete.html', {'variable':grupo, 'username':request.user.username})
	return render(request, 'base.html')

def ListGrupo(request):
	if request.user.is_authenticated:
		grupo = Grupo.objects.all()
		contexto = {'grupos':grupo, 'username':request.user.username}
		return render(request, 'listar_grupos.html', contexto)
	return render(request, 'base.html')

def paginador_Query(request, id_pagina):
	iterador = Musico.objects.all()
	musicos_por_pag = 5
	num_paginas = iterador.count() % musicos_por_pag
	if num_paginas == 0:
		paginador = 0 
	else:
		paginador = range(1, int(iterador.count() / musicos_por_pag + 2))

	pag = int(id_pagina) - 1
	inicio = pag*5
	fin = inicio+4
	iterador_final = Musico.objects.all()[inicio:fin]
	musicos_por_pag = 5
	num_paginas = iterador.count() % musicos_por_pag

	if request.user.is_authenticated:
		context = {
			"lista": iterador_final,
			"paginador": paginador,
			"musicos_por_pag": musicos_por_pag,
			"username":request.user.username
		}
	else:
		context = {
			"lista": iterador_final,
			"paginador": paginador,
			"musicos_por_pag": musicos_por_pag,
		}
	
    
	return render(request, 'musicos_Query.html', context)

def paginador_ajax(request):
	iterador = Musico.objects.all()
	iterador_final = Musico.objects.all()[0:5]

	musicos_por_pag = 5
	num_paginas = iterador.count() % musicos_por_pag

	if num_paginas == 0:
		paginador = range(1, int(iterador.count() / musicos_por_pag + 1))
	else:
		paginador = range(1, int(iterador.count() / musicos_por_pag + 2))

	if request.user.is_authenticated:
		context = {
			"lista": list(iterador_final),
			"paginador": paginador,
			"username":request.user.username
		}
	else:
		context = {
			"lista": list(iterador_final),
			"paginador": paginador,
		}
    
	return render(request, 'musicos_ajax.html', context)
def reclamaDatos(request, id_pagina):
	pag = int(id_pagina) - 1
	inicio = pag*5
	fin = inicio+5
	iterador_final = Musico.objects.all()[inicio:fin]
	datos = serializers.serialize('json',iterador_final)
	return HttpResponse(json.dumps({'musicos': datos}), content_type="application/json")	

def mapas(request):
	if request.user.is_authenticated:
		return render(request, 'mapa.html', {"username":request.user.username})
	return render(request, 'base.html')

def graficas(request):
	if request.user.is_authenticated:
		grupos = Grupo.objects.all()
	
		i = 0
		albums = [None] * grupos.count()
		for grupo in grupos:
			albums[i] = Album.objects.filter(grupo=grupo.id).count()
			i += 1

		context = {
			"grupos": grupos,
			"albums": albums,
			"username":request.user.username
		}
		return render(request, 'graficas.html', context)
	return render(request, 'base.html')
	