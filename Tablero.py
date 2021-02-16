import numpy as np

class Tablero:

    def __init__(self, dimension, barcos = []):

        self.matriz = np.zeros(dimension**2).reshape(dimension, dimension)
        self.barcos = barcos
        self.colocar_barcos()

    def coloca_barco(self, barco):

        cadena_letras = "ABCDEFGHIJ"

        x = barco.posicion[0] - 1

        y = cadena_letras.index(barco.posicion[1])

        if barco.axis == 0:

            self.matriz[x:barco.eslora + x, y] = 1

        else:

            self.matriz[x, y:barco.eslora + y] = 1

    def colocar_barcos(self):

        for barco in self.barcos:

            self.coloca_barco(barco)

    def imprimir_tablero(self):

        print(self.matriz)