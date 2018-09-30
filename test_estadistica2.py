from unittest import TestCase
from KataSimple import Estadistica

# Devolver un arreglo con el numero de elementos y el minimo


class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None], "cadena vacia")

    def test_getArregloUnNumero(self):
        self.assertEqual(Estadistica().getArreglo("1"), [1, 1], "Un numero Y UNO")

    # Ciclo TDD para que funcione con un string de 2 numeros

    def test_getArregloDosNumeros(self):
        self.assertEqual(Estadistica().getArreglo("1,3"), [2, 1], "Dos numeros, 1 y 1")