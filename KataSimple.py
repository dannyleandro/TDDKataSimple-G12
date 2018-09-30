class Estadistica:

    def getArreglo(self, cadena):
        if cadena == '':
            return [0]
        elif len(cadena) > 1:
            return [len(cadena)-1]
        else:
            return [int(cadena)]
