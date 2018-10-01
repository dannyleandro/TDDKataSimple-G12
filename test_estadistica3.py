from unittest import TestCase
from KataSimple import Estadistica


# Devolver un arreglo con el numero de elementos, el minimo y el maximo
class TestEstadistica(TestCase):
    def test_getArreglo(self):
        self.assertEqual(Estadistica().getArreglo(""), [0, None, None], "cadena vacia")

    def test_getArregloUnNumero(self):
        self.assertEqual(Estadistica().getArreglo("1"), [1, 1, 1], "Un numero Y UNO")

    # Ciclo TDD para que funcione con un string de 2 numeros

    def test_getArregloDosNumeros(self):
        self.assertEqual(Estadistica().getArreglo("1,3"), [2, 1, 3], "Dos numeros, 2 y 1,3")

    # Ciclo TDD para que funcione con un string de N numeros

    def test_getArregloNNumeros(self):
        self.assertEqual(Estadistica().getArreglo("6,7,3"), [3, 3, 7], "Tres numeros ")
        self.assertEqual(Estadistica().getArreglo("4,6,5,1"), [4, 1, 6], "Cuatro numeros ")
        self.assertEqual(Estadistica().getArreglo("9,8,2,45,10"), [5, 2, 45], "Cinco numeros ")