from unittest import TestCase
from KataSimple import Estadistica


class TestEstadistica(TestCase):
    def test_getArregloVacio(self):
        self.assertEqual(Estadistica().getArreglo(""),[0], "cadena vacia")
