from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Aventurero, Item, Montura
from django.urls import reverse
from django.db.models import Max

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def aventureros(request):
    letra = request.GET.get('letra', None)
    if (letra == None):
        aventureros = Aventurero.objects.all().values()
        # Devuelve una QuerySet no una lista de aventureros
        # aventureros = Aventurero.objects.raw('SELECT * FROM members_aventurero')
    else:
        letra = letra + '%'
        aventureros = Aventurero.objects.raw('SELECT * FROM members_aventurero WHERE nombre LIKE %s AND vida > 200',[letra])
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
        'aventurero' : aventurero,
        'items' : items,
        'aventureros' : aventureros
    }
    return HttpResponse(template.render(context, request))

def addAventurero(request):
    template = loader.get_template('addAventurero.html')
    return HttpResponse(template.render({},request))


def atacar(request, id_atacante, id_atacado):
    atacado = Aventurero.objects.get(id=id_atacado)
    items = Item.objects.all().filter(aventurero_id=id_atacante)
    item = items.order_by('da??o').first()

    if (item != None):
        atacado.recibirAtaque(item.da??o)
        atacado.save()
        return HttpResponseRedirect(reverse('aventureros'))
    return HttpResponse("El aventurero no tiene items")


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
    y = request.POST['da??o']
    z = request.POST['Id_Due??o']
    aventurero = Aventurero.objects.get(id=z)
    if (aventurero == None):
        return HttpResponse("Ese aventurero no existe")
    item = Item(nombre = x, da??o = y, aventurero = aventurero)
    item.save()
    return HttpResponseRedirect(reverse ('items'))

def monturas(request):
    monturas = Montura.objects.all().values()
    template = loader.get_template('monturas.html')
    context = {
        'monturas' : monturas
    }
    return HttpResponse(template.render(context,request))