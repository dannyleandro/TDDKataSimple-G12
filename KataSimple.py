class Estadistica:

    def getArreglo(self, cadena):
        if cadena == '':
            return [0, None]
        else:
            result = cadena.split(',')
            return [len(result)]
