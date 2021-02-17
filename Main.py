from Jugador import *

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

    cadena_letras = "ABCDEFGHIJ"

    x = posicion[0] - 1

    y = cadena_letras.index(posicion[1])

    return (x, y)

jugador_1 = Jugador()

jugador_2 = Jugador()

jugador_1.imprimir_tablero()

jugador_2.imprimir_tablero()

disparar((1,"D"), jugador_1, jugador_2)

jugador_1.imprimir_tablero()

jugador_2.imprimir_tablero()