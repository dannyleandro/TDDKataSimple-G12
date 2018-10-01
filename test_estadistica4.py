from unittest import TestCase
from KataSimple import Estadistica


# Devolver un arreglo con el numero de elementos, el minimo,  el maximo y el promedio
class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None, None, None], "cadena vacia")

    def test_getArregloUnNumero(self):
        self.assertEqual(Estadistica().getArreglo("1"), [1, 1, 1, 1], "Un numero Y UNO")

    # Ciclo TDD para que funcione con un string de 2 numeros

    def test_getArregloDosNumeros(self):
        self.assertEqual(Estadistica().getArreglo("1,3"), [2, 1, 3, 2], "Dos numeros, 2 y 1,3")