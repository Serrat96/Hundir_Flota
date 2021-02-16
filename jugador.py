from Tablero import *
from Barco import *
import Constantes as ct

class Jugador:

    tablero_barcos = None
    tablero_disparos = None
    vidas = 0
    def __init__(self):
        self.tablero_barcos = Tablero(10,self.createListBarcosDefault())
        self.tablero_disparos = Tablero(10)
        self.vidas = len(self.tablero_barcos.posicion_barcos)


    def createListBarcosDefault(self):
        array_barcos_1_pos = np.array([Barco((1, 'C'), 1), Barco((3, 'H'), 1), Barco((6, 'I'), 1), Barco((8, 'C'), 1)])

        array_barcos_2_pos = np.array([Barco((1, 'F'), 2, 0), Barco((1, 'I'), 2, 0), Barco((10, 'G'), 2, 1)])

        array_barcos_3_pos = np.array([Barco((3, 'A'), 3, 0), Barco((5, 'E'), 3, 1)])

        array_barcos_4_pos = np.array([Barco((8, 'F'), 4, 1)])

        return np.concatenate(
            (array_barcos_1_pos, array_barcos_2_pos, array_barcos_3_pos, array_barcos_4_pos))

    def printTableros(self):
        self.printTablero(self.tablero_barcos)
        print("")
        self.printTablero(self.tablero_disparos)
        print("")

    def printTablero(self, tablero):
        matriz = tablero.matriz
        to_print = ['\t'] + ct.REF_CHARS
        print(*to_print)

        for index, row in enumerate(matriz):
            to_print = [str(ct.REF_NUMBERS[index])+"\t"]
            for val in row:
                #to_print += str(int(val))
                to_print += val
            print(*to_print)


    def shotIn(self, posicion):

        auxPos = str(posicion[0]) + str(posicion[1])

        if auxPos in self.tablero_barcos.posicion_barcos:
            self.vidas -= 1
            self.tablero_barcos.write(posicion, ct.TOCADO)
        else:
            self.tablero_barcos.write(posicion, ct.AGUA)

