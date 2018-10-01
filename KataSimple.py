class Estadistica:

    def getArreglo(self, cadena):
        result = cadena.split(',')
        min = 9999
        if cadena == '':
            return [0, None, None]
        elif len(result) == 1:
            return [1, int(cadena), int(cadena)]
        elif len(result) == 2:
            if int(result[0]) > int(result[1]):
                return [2, int(result[1]), int(result[0])]
            else:
                return [2, int(result[0]), int(result[1])]
        else:
            for x in result:
                if int(x) < min:
                    min = int(x)
            return [len(result), min]
