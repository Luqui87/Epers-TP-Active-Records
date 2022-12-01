from django.urls import path
from . import views

urlpatterns = [
    # ex: /members/
    path('', views.index, name='index'),

# ex: /members/
    path('aventureros/', views.aventureros, name='aventureros'),

    path('aventureros/add/', views.addAventurero, name='addAventurero'),

    path('aventureros/add/addrecord/', views.addAventureroPost, name='addAventurero'),

    # ex: /members/aventureros/5/
    path('aventureros/<int:aventurero_id>', views.aventurero, name= 'aventurero'),

    path('aventureros/<int:id_atacante>/attack/<int:id_atacado>', views.atacar),

    path('aventureros/delete/<int:id>', views.delete, name='delete'),

    #ex: /members/item/1/
    path('items/<int:item_id>', views.item, name = 'item'),
    #ex: /members/item/1/
    path('items/', views.items, name = 'items'),

    path('items/add/', views.addItem, ),

    path('items/add/addrecord/', views.addItemPost),
]