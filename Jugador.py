
from Tablero import *
import Constantes as cs

class Jugador:

    def __init__(self):

        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.coloca_barcos_random()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []

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
