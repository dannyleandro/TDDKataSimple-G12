from unittest import TestCase
from KataSimple import Estadistica


class TestEstadistica(TestCase):
    def test_getArregloVacio(self):
        self.assertEqual(Estadistica().getArreglo(""), [0], "cadena vacia")

    def test_getArregloUnNumero(self):
            self.assertEqual(Estadistica().getArreglo("1"), [1], "Un numero")

    # Ciclo TDD para que funcione con un string de 2 numeros

    def test_getArregloDosNumeros(self):
        self.assertEqual(Estadistica().getArreglo("1,3"), [2], "Dos numeros")


    # Ciclo TDD para que funcione con un string de N numeros

    def test_getArregloNNumeros(self):
        self.assertEqual(Estadistica().getArreglo("1,3,5"), [3], "Tres numeros")
        self.assertEqual(Estadistica().getArreglo("1,3,5,45"), [4], "Cuatro numeros")
        self.assertEqual(Estadistica().getArreglo("1,3,5,45,10"), [5], "Cinco numeros")



