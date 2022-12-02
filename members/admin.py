from django.contrib import admin

# Register your models here.

from .models import Item
from .models import Aventurero, Montura

admin.site.register(Item)
admin.site.register(Aventurero)
admin.site.register(Montura)
