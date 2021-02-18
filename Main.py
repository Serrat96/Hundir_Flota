from Jugador import *
import random
import Constantes as cs
from time import sleep
from tqdm import tqdm

def disparar(posicion, de_jugador, a_jugador):

    posicion_traducida = traducir_posicion(posicion)

    if a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] == "1":

        de_jugador.tablero_disparos.matriz[posicion_traducida[0],posicion_traducida[1]] = "X"

        a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] = "X"

        a_jugador.vidas -= 1

        return True

    else:

        de_jugador.tablero_disparos.matriz[posicion_traducida[0],posicion_traducida[1]] = "Ø"

        a_jugador.tablero_barcos.matriz[posicion_traducida[0],posicion_traducida[1]] = "Ø"

        return False

def traducir_posicion(posicion):

    x = posicion[0] - 1

    y = cs.LISTA_CARACTERES.index(posicion[1])

    return (x, y)

def posicion_random():

    x = random.randint(1, 10)
    y = cs.LISTA_CARACTERES[random.randint(0, 9)]

    return (x, y)

es_maquina = False

jugador_1 = Jugador()

jugador_2 = Jugador()

print("Bienvenido al juego HUNDIR LA FLOTA")

print("                  __--___\n\
                 >_--__ \n\
                _________!__________\n\
               /   /   /   /   /   /\n\
              /   /   /   /   /   /\n\
             |   |   |   |   |   |\n\
        __^  |   |   |   |   |   |\n\
      _/@  \  \   \   \   \   \   \n\
     S__   |   \   \   \   \   \   \         __\n\
    (   |  |    \___\___\___\___\___\       /  \n\
        |   \             |                |  |\|\n\
        \    \____________!________________/  /\n\
         \ _______OOOOOOOOOOOOOOOOOOO________/\n\
          \_________________________________/\n\
%%%^^^^^%%%%%^^^^!!^%%^^^^%%%%%!!!!^^^^^^!%^^^%%%%!!^^\n\
^^!!!!%%%%^^^^!!^^%%%%%^^!!!^^%%%%%!!!%%%%^^^!!^^%%%!\n")

sleep(0.5)

print("Los símbolos '=' hacen referncia al agua")

sleep(0.5)

print("El símbolo 'Ø' hace referencia a un disparo fallido")

sleep(0.5)

print("El símbolo 'X' hace referencia a un barco tocado")

sleep(0.5)

input("Presiona enter para continuar: ")
jugador_1.barcos_random()

print("CARGANDO...")
for i in tqdm(range(10)):
    sleep(0.5)

"""while jugador_1.vidas > 0 and jugador_2.vidas > 0:

    jugador_1.imprimir_tablero()

    

    jugador_2.imprimir_tablero()

   if not es_maquina:

        posicion = str(input("Introduzca la coordenada a la que desea diparar: "))

        tupla_posicion = (int(posicion[0]), posicion[1])

        resultado = disparar(tupla_posicion, jugador_1, jugador_2)

        if resultado:

            es_maquina = False

            if jugador_2.vidas != 0:

                print("¡HAS ACERTADO!, te toca tirar de nuevo")

        else:

            print("No has acertado, pasa el turno a la CPU: ")

            es_maquina = True

    else:

        tupla_posicion = posicion_random()

        print("La CPU ha disparado a: ", tupla_posicion)

        disparar(tupla_posicion, jugador_2, jugador_1)

        print("Calculando disparo de la CPU")

        sleep(3)

        if not resultado:

            print("La CPU no ha acertado, se pasa el turno al jugador: ")

            es_maquina = False

        else:
            print("La CPU ha acertado, le toca tirar de nuevo")

            es_maquina = True

            sleep(0.5)

if es_maquina:

    print("La máquina ha ganado... Vuelve a jugar que es gratis")

else:

    print("¡ENHORABUENA!, HAS GANADO")"""