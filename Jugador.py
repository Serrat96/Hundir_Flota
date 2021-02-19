import numpy as np
import random
from Barco import *
from Tablero import *
import Constantes as cs

class Jugador:

    def __init__(self):

        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.coloca_barcos_random()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []


    # def barcos(self):
    #
    #     array_barcos_1_pos = np.array([Barco((1, 'C'), 1), Barco((3, 'H'), 1), Barco((6, 'I'), 1), Barco((8, 'C'), 1)])
    #
    #     array_barcos_2_pos = np.array([Barco((1, 'F'), 2, 0), Barco((1, 'I'), 2, 1), Barco((10, 'G'), 2, 1)])
    #
    #     array_barcos_3_pos = np.array([Barco((3, 'A'), 3, 0), Barco((5, 'E'), 3, 1)])
    #
    #     array_barcos_4_pos = np.array([Barco((8, 'F'), 4, 1)])
    #
    #     return np.concatenate((array_barcos_1_pos, array_barcos_2_pos, array_barcos_3_pos, array_barcos_4_pos))

    def imprimir_tablero(self):
        titulo = np.array(cs.LISTA_CARACTERES)
        print("  ",titulo, "           ",titulo)
        print("")
        for i in range(len(cs.LISTA_NUMEROS)):
            if i != 9:
                numero = str(cs.LISTA_NUMEROS[i]) + " "
            else:
                numero = str(cs.LISTA_NUMEROS[i])

            print(numero, self.tablero_barcos.matriz[i],
                  "        ", numero, self.tablero_disparos.matriz[i])

        print("\n")

    '''def posicion_random(self):

        x = random.randint(0, 9)

        y = random.randint(0, 9)

        return (x, y)

    def barcos_random(self):

        for propiedades in cs.TIPOS_BARCO:

            contador = 0

            while contador < propiedades[1]:

                posicion = self.posicion_random()

                x = posicion[0]

                y = posicion[1]

                slicing_sur = self.tablero_barcos.matriz[x: x + propiedades[0], y]

                slicing_norte = self.tablero_barcos.matriz[x: x - propiedades[0]:-1, y]

                slicing_este = self.tablero_barcos.matriz[x, y: y + propiedades[0]]

                slicing_oeste = self.tablero_barcos.matriz[x, y:y - propiedades[0]:-1]

                if cs.BARCO_CHAR not in slicing_sur and len(slicing_sur) == propiedades[0]:

                    self.tablero_barcos.matriz[x: x + propiedades[0], y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_norte and len(slicing_norte) == propiedades[0]:

                    self.tablero_barcos.matriz[x: x - propiedades[0]:-1, y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_este and len(slicing_este) == propiedades[0]:

                    self.tablero_barcos.matriz[x, y: y + propiedades[0]] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_oeste and len(slicing_oeste) == propiedades[0]:

                    self.tablero_barcos.matriz[x, y:y - propiedades[0]:-1] = cs.BARCO_CHAR
                    contador += 1'''

    def disparar(self, posicion, a_jugador):

        self.disparos.append(posicion)

        posicion_traducida = self.traducir_posicion(posicion)


        if a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] == cs.BARCO_CHAR:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.TOCADO_CHAR

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.TOCADO_CHAR

            a_jugador.vidas -= 1

            return True

        else:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.FALLO_CHAR

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.FALLO_CHAR

            return False

    def traducir_posicion(self, posicion):

        x = posicion[0] - 1

        y = cs.LISTA_CARACTERES.index(posicion[1])

        return (x, y)
