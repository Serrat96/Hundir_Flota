
import Tablero
from Barco import *
import numpy as np
#barco = Barco((1,'F'),1)
array_barcos_1_pos = np.array([Barco((1,'C'), 1), Barco((3,'H'), 1), Barco((6,'I'), 1), Barco((8,'C'), 1)])

array_barcos_2_pos = np.array([Barco((1,'F'), 2, 0), Barco((1,'I'), 2, 0), Barco((10,'G'), 2, 1)])

array_barcos_3_pos = np.array([Barco((3,'A'), 3, 0), Barco((5,'E'), 3, 1)])

array_barcos_4_pos = np.array([Barco((8,'F'), 4, 0)])

array_barcos_total = np.concatenate((array_barcos_1_pos, array_barcos_2_pos, array_barcos_3_pos, array_barcos_4_pos))

"""tablero_barco_j1 = Tablero(10, )

tablero_disparos_j1 =

tablero_barco_j2 =

tablero_disparos_j2 ="""

print(array_barcos_total)