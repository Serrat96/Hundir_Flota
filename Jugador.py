import numpy as np
from Barco import *
from Tablero import *
class Jugador:

    def __init__(self):

        self.tablero_barcos = Tablero(10, self.barcos())
        self.tablero_disparos = Tablero(10)


    def barcos(self):

        array_barcos_1_pos = np.array([Barco((1, 'C'), 1), Barco((3, 'H'), 1), Barco((6, 'I'), 1), Barco((8, 'C'), 1)])

        array_barcos_2_pos = np.array([Barco((1, 'F'), 2, 0), Barco((1, 'I'), 2, 1), Barco((10, 'G'), 2, 1)])

        array_barcos_3_pos = np.array([Barco((3, 'A'), 3, 0), Barco((5, 'E'), 3, 1)])

        array_barcos_4_pos = np.array([Barco((8, 'F'), 4, 1)])

        return np.concatenate((array_barcos_1_pos, array_barcos_2_pos, array_barcos_3_pos, array_barcos_4_pos))

    def tablero_barcos(self):
        pass

    def imprimir_tablero(self):

        print(self.tablero_barcos.matriz)






