import numpy as np
import Constantes as cs
import random

class Tablero:

    def __init__(self, dimension, barcos=[]):

        self.dimension = dimension
        self.matriz = np.full((dimension, dimension), cs.AGUA_CHAR)
        self.barcos = barcos

    def posicion_random(self):

        x = random.randint(0, 9)

        y = random.randint(0, 9)

        return (x, y)

    def coloca_barcos_random(self):

        for propiedades in cs.TIPOS_BARCO:

            contador = 0

            while contador < propiedades[1]:

                posicion = self.posicion_random()

                x = posicion[0]

                y = posicion[1]

                slicing_sur = self.matriz[x: x + propiedades[0], y]

                slicing_norte = self.matriz[x: x - propiedades[0]:-1, y]

                slicing_este = self.matriz[x, y: y + propiedades[0]]

                slicing_oeste = self.matriz[x, y:y - propiedades[0]:-1]

                if cs.BARCO_CHAR not in slicing_sur and len(slicing_sur) == propiedades[0]:

                    self.matriz[x: x + propiedades[0], y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_norte and len(slicing_norte) == propiedades[0]:

                    self.matriz[x: x - propiedades[0]:-1, y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_este and len(slicing_este) == propiedades[0]:

                    self.matriz[x, y: y + propiedades[0]] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_oeste and len(slicing_oeste) == propiedades[0]:

                    self.matriz[x, y:y - propiedades[0]:-1] = cs.BARCO_CHAR
                    contador += 1

    def imprimir_tablero(self):

        print(self.matriz)

    def coloca_barco(self, barco):

        cadena_letras = "ABCDEFGHIJ"

        x = barco.posicion[0] - 1

        y = cadena_letras.index(barco.posicion[1])

        if barco.axis == 0:

            self.matriz[x:barco.eslora + x, y] = cs.BARCO_CHAR

        else:

            self.matriz[x, y:barco.eslora + y] = cs.BARCO_CHAR

    def coloca_barcos(self):

        for barco in self.barcos:

            self.coloca_barco(barco)

