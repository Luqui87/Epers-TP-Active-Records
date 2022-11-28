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
    return HttpResponse("Estas son las stats del aventurero %s." % aventurero_id)

def item(request, item_id):
    return HttpResponse("Estas son las stats del item %s" % item_id)

def addAventurero(request):
    template = loader.get_template('addAventurero.html')
    return HttpResponse(template.render({},request))

def items(request,):
    items = Item.objects.all().values()
    template = loader.get_template('items.html')
    context = {
        'items' : items
    }
    return HttpResponse(template.render(context,request))