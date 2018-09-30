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


    # Ciclo TDD para que funcione con un string de N numeros

    def test_getArregloNNumeros(self):
        self.assertEqual(Estadistica().getArreglo("6,7,3"), [3, 3], "Tres numeros 3,1")
        self.assertEqual(Estadistica().getArreglo("4,6,5,1"), [4, 1], "Cuatro numeros 4,1")
        self.assertEqual(Estadistica().getArreglo("9,8,2,45,10"), [5, 2], "Cinco numeros 5,2")