import numpy as np

class Tablero:

    def __init__(self, dimension,  barcos):

        self.matriz = np.zeros(dimension**2).reshape(dimension, dimension)
        self.barcos = barcos
