import numpy as np
import random
from Barco import *
from Tablero import *
import Constantes as cs

class Jugador:

    def __init__(self):

        self.tablero_barcos = Tablero(10, self.barcos())
        self.tablero_disparos = Tablero(10)
        self.vidas = 20

    def barcos(self):

        array_barcos_1_pos = np.array([Barco((1, 'C'), 1), Barco((3, 'H'), 1), Barco((6, 'I'), 1), Barco((8, 'C'), 1)])

        array_barcos_2_pos = np.array([Barco((1, 'F'), 2, 0), Barco((1, 'I'), 2, 1), Barco((10, 'G'), 2, 1)])

        array_barcos_3_pos = np.array([Barco((3, 'A'), 3, 0), Barco((5, 'E'), 3, 1)])

        array_barcos_4_pos = np.array([Barco((8, 'F'), 4, 1)])

        return np.concatenate((array_barcos_1_pos, array_barcos_2_pos, array_barcos_3_pos, array_barcos_4_pos))

    def imprimir_tablero(self):

        for i in range(len(self.tablero_barcos.matriz)):

            print(self.tablero_barcos.matriz[i], "         ", self.tablero_disparos.matriz[i])

        print("\n")

    def posicion_random(self):

        x = random.randint(0, 9)

        y = random.randint(0, 9)

        z = random.randint(0,1)

        return (x, y, z)

    def barcos_random(self):

        for propiedades in cs.TIPOS_BARCO:

            posicion = self.posicion_random()

            x = posicion[0]

            y = posicion[1]

            z = posicion[2]

            slicing_horizontal = self.tablero_barcos.matriz[x : x + propiedades[0], y]

            print(slicing_horizontal)
