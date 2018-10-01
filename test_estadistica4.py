from unittest import TestCase
from KataSimple import Estadistica


# Devolver un arreglo con el numero de elementos, el minimo,  el maximo y el promedio
class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None, None, None], "cadena vacia")
