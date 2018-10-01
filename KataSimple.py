class Estadistica:

    def getArreglo(self, cadena):
        result = cadena.split(',')
        min = 9999
        max = 0
        if cadena == '':
            return [0, None, None, None]
        elif len(result) == 1:
            return [1, int(cadena), int(cadena), int(cadena)]
        else:
            for x in result:
                if int(x) < min:
                    min = int(x)
            for x in result:
                if int(x) > max:
                    max = int(x)
            return [len(result), min, max]
