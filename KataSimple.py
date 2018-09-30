class Estadistica:

    def getArreglo(self, cadena):
        result = cadena.split(',')
        if cadena == '':
            return [0, None]
        elif len(cadena) > 1:
            if result[0] < result[1]:
                return [len(result), int(result[0])]
            else:
                return [len(result), int(result[1])]
        else:
            return [len(result), int(cadena)]
