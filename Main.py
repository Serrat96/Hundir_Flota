from Jugador import *
import random
import Constantes as cs
from time import sleep
from tqdm import tqdm

def posicion_random():

    x = random.randint(1, 10)
    y = cs.LISTA_CARACTERES[random.randint(0, 9)]

    return (x, y)


def lee_input(jugador, posicion):

    resp = None

    try:
        if len(posicion) == 3:
            if int(posicion[0:2]) == 10 and posicion[2].upper() in cs.LISTA_CARACTERES:
                resp = (int(posicion[0:2]), posicion[2].upper())

        elif len(posicion) == 2:
            if int(posicion[0]) > 0 and int(posicion[0]) < 10 and posicion[1].upper() in cs.LISTA_CARACTERES:
                resp = (int(posicion[0]), posicion[1].upper())

        elif posicion == "0":

            resp = 0

        if resp in jugador.disparos:
            print("Ya has disparado en esta posicion")
            resp = None

        return resp
    except:
        return None

es_maquina = False

salir = False

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
      _/@  \  \   \   \   \   \   \ \n\
     S__   |   \   \   \   \   \   \         ___ \n\
       |  |    \___\___\___\___\___\       /   \ \n\
        |   \             |                |  |\|\n\
        \    \____________!________________/  /\n\
         \ _________HUNDIR LA FLOTA__________/\n\
          \________BY JAVIER & SERRAT_______/\n\
%%%^^^^^%%%%%^^^^!!^%%^^^^%%%%%!!!!^^^^^^!%^^^%%%%!!^^\n\
^^!!!!%%%%^^^^!!^^%%%%%^^!!!^^%%%%%!!!%%%%^^^!!^^%%%!\n")

sleep(0.5)

print("Los símbolos '~' hacen referncia al agua")

sleep(0.5)

print("El símbolo 'Ø' hace referencia a un disparo fallido")

sleep(0.5)

print("El símbolo 'X' hace referencia a un barco tocado")

sleep(0.5)

input("Presiona enter para continuar")

print("CARGANDO...")
for i in tqdm(range(10)):
    sleep(0.5)

while jugador_1.vidas > 0 and jugador_2.vidas > 0 :

    if not es_maquina:
        jugador_1.imprimir_tablero()

        while True:
            print("SALIR = 0")
            posicion = str(input("Introduzca la coordenada a la que desea diparar (ej. 10f): "))

            tupla_posicion = lee_input(jugador_1, posicion)

            if tupla_posicion != None:

                break

            else:
                print ("Entrada no válida")

        if tupla_posicion == 0:

            salir = True

            break

        resultado = jugador_1.disparar(tupla_posicion, jugador_2)

        if resultado:

            es_maquina = False

            if jugador_2.vidas != 0:

                print("¡HAS ACERTADO!, te toca tirar de nuevo")

        else:

            print("No has acertado, pasa el turno a la CPU: ")

            es_maquina = True

    else:
        print("Turno de la CPU")

        apuntar = False

        while not apuntar:

            tupla_posicion = posicion_random()

            if not tupla_posicion in jugador_2.disparos:

                apuntar =True

        print("La CPU está apuntando a: ", tupla_posicion)

        resultado = jugador_2.disparar(tupla_posicion, jugador_1)


        sleep(3)

        if not resultado:

            print("La CPU no ha acertado, se pasa el turno al jugador: ")

            es_maquina = False

        else:
            print("La CPU ha acertado, le toca tirar de nuevo")

            es_maquina = True

            sleep(0.5)

if es_maquina and not salir:

    print("La máquina ha ganado... Vuelve a jugar que es gratis")

elif not es_maquina and not salir:

    print("¡ENHORABUENA!, HAS GANADO")

elif salir:

    print("Fin del juego")