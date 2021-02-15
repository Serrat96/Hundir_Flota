import numpy as np
class Tablero:

    def __init__(self, dimension, barcos):

        self.matriz = np.zeros(100).reshape(10, 10)
        self.barcos = barcos