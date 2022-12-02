from django.test import TestCase
from members.models import Aventurero, Item

class AventureroTestCase(TestCase):
    aventurero = None

    def setUp(self):
        Aventurero.objects.create(nombre = "Roland", vida = 200)
        self.aventurero = Aventurero.objects.get(nombre="Roland")

    def test_Guardar_Y_Recuperar(self):
        self.assertEqual(self.aventurero.nombre , "Roland")
        self.assertEqual(self.aventurero.vida, 200)

    def test_Recibir_Ataque(self):
        self.aventurero.recibirAtaque(100)
        self.assertEqual(self.aventurero.vida, 100)

    def test_Recibir_Ataque_Mayor_A_Vida(self):
        self.aventurero.recibirAtaque(300)
        self.assertEqual(self.aventurero.vida, 0)


class ItemTestCase(TestCase):
    aventurero = None
    item = None

    def setUp(self):
        Aventurero.objects.create(nombre="Roland", vida=200)
        self.aventurero = Aventurero.objects.get(nombre="Roland")
        Item.objects.create(nombre="Pistola", daño = 200, aventurero = self.aventurero)
        self.item = Item.objects.get(nombre = "Pistola")

    def test_Recuperar_Item(self):
        self.assertEqual(self.item.nombre, "Pistola" )
        self.assertEqual(self.item.daño, 200)
        self.assertEqual(self.item.aventurero, self.aventurero)


