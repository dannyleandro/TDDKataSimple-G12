from unittest import TestCase
from KataSimple import Estadistica

# 2.  Devolver un arreglo con el numero de elementos y el minimo


class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None], "cadena vacia")
