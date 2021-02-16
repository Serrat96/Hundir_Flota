import numpy as np
import Constantes as ct


class Tablero:

    posicion_barcos = set()

    def __init__(self, dimension,  barcos = []):

        self.dimension = dimension
        #self.matriz = np.zeros(dimension ** 2).reshape(dimension, dimension)
        self.matriz = np.full(fill_value = '=', shape= (10,10))
        self.barcos = barcos
        self.setBarcos()
        self.vidas = len(self.posicion_barcos)


    def setBarcos(self):
        for barco in self.barcos:
            self.setBarco(barco)

    def setBarco(self, barco):

        numberTranslateNumber = ct.REF_NUMBERS.index(barco.posicion[0])
        charTranslateNumber = ct.REF_CHARS.index(barco.posicion[1])

        cont = 0
        while cont < barco.eslora:
            if barco.axis == 0:
                self.matriz[numberTranslateNumber + cont][charTranslateNumber] = ct.BARCO

                self.posicion_barcos.add(str(ct.REF_NUMBERS[numberTranslateNumber + cont]) +
                                            ct.REF_CHARS[charTranslateNumber])
            else:

                self.matriz[numberTranslateNumber][charTranslateNumber + cont] = ct.BARCO

                self.posicion_barcos.add(str(ct.REF_NUMBERS[numberTranslateNumber]) +
                                            ct.REF_CHARS[charTranslateNumber + cont])
            cont += 1


    def write(self, posicion, contenido):
        numberTranslateNumber = ct.REF_NUMBERS.index(posicion[0])
        charTranslateNumber = ct.REF_CHARS.index(posicion[1])
        self.matriz[numberTranslateNumber][charTranslateNumber] = contenido
