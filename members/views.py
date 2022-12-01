from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Aventurero, Item
from django.urls import reverse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def aventureros(request):
    aventureros = Aventurero.objects.all().values()
    # Devuelve una QuerySet no una lista de aventureros
    # aventureros = Aventurero.objects.raw('SELECT * FROM members_aventurero')
    template = loader.get_template('aventureros.html')
    context = {
        'aventureros':aventureros
    }
    return HttpResponse(template.render(context, request))

def addAventureroPost(request):
    x = request.POST['nombre']
    y = request.POST['vida']
    aventurero = Aventurero(nombre=x, vida=y)
    aventurero.save()
    return HttpResponseRedirect(reverse ('aventureros'))

def delete(request,id):
    aventurero = Aventurero.objects.get(id=id)
    aventurero.delete()
    return HttpResponseRedirect(reverse('aventureros'))

def aventurero(request, aventurero_id):
    aventurero = Aventurero.objects.get(id=aventurero_id)
    items = Item.objects.all().filter(aventurero_id = aventurero_id)
    aventureros = Aventurero.objects.exclude(id = aventurero_id)
    template = loader.get_template('aventurero.html')
    context = {
        'nombre': aventurero.nombre,
        'vida': aventurero.vida,
        'items' : items,
        'aventureros' : aventureros
    }
    return HttpResponse(template.render(context, request))

def addAventurero(request):
    template = loader.get_template('addAventurero.html')
    return HttpResponse(template.render({},request))


def item(request, item_id):
    return HttpResponse("Estas son las stats del item %s" % item_id)


def items(request,):
    items = Item.objects.all().values()
    template = loader.get_template('items.html')
    context = {
        'items' : items
    }
    return HttpResponse(template.render(context,request))

def addItem(request):
    template = loader.get_template('addItem.html')
    return HttpResponse(template.render({},request))

def addItemPost(request):
    x = request.POST['nombre']
    y = request.POST['daño']
    z = request.POST['Id_Dueño']
    aventurero = Aventurero.objects.get(id=z)
    item = Item(nombre = x, daño = y, aventurero = aventurero)
    item.save()
    return HttpResponseRedirect(reverse ('items'))
