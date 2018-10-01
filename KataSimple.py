class Estadistica:

    def getArreglo(self, cadena):
        result = cadena.split(',')
        min = 9999
        if cadena == '':
            return [0, None, None]
        else:
            for x in result:
                if int(x) < min:
                    min = int(x)

            return [len(result), min]
