from django.db import models

# Create your models here.



class Aventurero(models.Model):
    nombre = models.CharField(max_length=100)
    vida = models.IntegerField(default=100)

    def __str__(self):
        return self.nombre

    def recibirAtaque(self, daño):
        if (self.vida > daño):
            self.vida -= daño
        else:
            self.vida = 0

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    daño = models.IntegerField(default=20)
    aventurero = models.ForeignKey(Aventurero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Montura(models.Model):
    nombre = models.CharField(max_length=60)
    velocidad = models.IntegerField(default=20)
    aventurero = models.OneToOneField(
        Aventurero,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def recibioDaño(self, daño):
        self.velocidad -= (daño/4)

    def __str__(self):
        return self.nombre