from django.db import models

# Create your models here.



class Aventurero(models.Model):
    nombre = models.CharField(max_length=100)
    vida = models.IntegerField(default=100)

    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    daño = models.IntegerField(default=20)
    aventurero = models.ForeignKey(Aventurero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre