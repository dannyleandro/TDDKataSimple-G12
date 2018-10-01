from unittest import TestCase
from KataSimple import Estadistica


# Devolver un arreglo con el numero de elementos, el minimo y el maximo
class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None, None], "cadena vacia")


    def test_getArregloUnNumero(self):
        self.assertEqual(Estadistica().getArreglo("1"), [1, 1, 1], "Un numero Y UNO")