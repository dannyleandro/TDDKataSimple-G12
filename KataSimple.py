class Estadistica:

    def getArreglo(self, cadena):
        if cadena == '':
            return [0]
        else:
            result = cadena.split(',')
            return [len(result)]
