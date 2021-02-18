from Jugador import *
import random
import Constantes as cs
import time

def disparar(posicion, de_jugador, a_jugador):

    posicion_traducida = traducir_posicion(posicion)

    if a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] == "1":

        de_jugador.tablero_disparos.matriz[posicion_traducida[0],posicion_traducida[1]] = "X"

        a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] = "X"

        a_jugador.vidas -= 1

    else:

        de_jugador.tablero_disparos.matriz[posicion_traducida[0],posicion_traducida[1]] = "Ø"

        a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] = "Ø"

def traducir_posicion(posicion):

    x = posicion[0] - 1

    y = cs.LISTA_CARACTERES.index(posicion[1])

    return (x, y)

def posicion_random():

    x = random.randint(1, 10)
    y = cs.LISTA_CARACTERES[random.randint(0, 9)]

    return (x, y)

jugador_1 = Jugador()

jugador_2 = Jugador()

while jugador_1.vidas > 0 and jugador_2.vidas > 0:

    jugador_1.imprimir_tablero()
    jugador_2.imprimir_tablero()

    posicion = str(input("Introduzca la coordenada a la que desea diparar: "))

    tupla_posicion = (int(posicion[0]), posicion[1])

    disparar(tupla_posicion, jugador_1, jugador_2)

    tupla_posicion = posicion_random()

    print(tupla_posicion)

    disparar(tupla_posicion, jugador_2, jugador_1)

    time.sleep(3)