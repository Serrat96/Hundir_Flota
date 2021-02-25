# Hundir_Flota
Juego de hundir la flota
## Clase Main
es la clase que se encarga de manejar la interfaz y el flujo del programa
### Contiene un par de métodos:
* posicion_random: crea una posición en un tablero de 10 x 10 de fila-letra
* lee_input: se le pasa como parámetros un jugador y una posición. este método comprueba la validez del disparo, no debe de haber disparado en esa misma posición y tiene que estar bien construido para que identifique una posición real del tablero

## Clase jugador
esta formado por dos tableros, uno para los disparos y otro para los barcos, una porpiedad de vidas que representa el número de disparos que hay que hacer para hundir todos los barcos, y una lista de disparos, que almacena los disparos que ha realizado el jugador.

### Los métodos:
* imprimir_tablero: se encarga de pintar los dos tableros propiedad del jugador de una forma legible
* disparar: como parámetros se le pasa la posición a la que se dispara y el jugador al que se dispara. Comprueba si se ha acertado y en ese caso resta la variable vida del jugador afectado
* traducir_posicion: se pasa como parámetro la posición numero letra que pasa el jugador y se traduce para leer en la matriz

## Clase Tablero
crea un tablero pasandole las dimensiones que se quieren, se puede pasar un listado de objetos barcos para que se coloquen (esto no se ha implementado en el juego, ya que se colocan de forma aleatoria)

### métodos:
* posicion_random: crea una posición dentro del tablero de forma aleatoria
* coloca_barcos_random: se encarga de colocar todos los barcos de forma aleatoria

## Archivo de constantes

#### LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J']
Sirve para traducir la posición de la letra a indice del tablero y para dibujar las referencias en la interfaz

#### LISTA_NUMEROS = [1,2,3,4,5,6,7,8,9,10]
Sirve para traducir la posición del número a indice del tablero y para dibujar las referencias en la interfaz

#### TIPOS_BARCO = [(4, 1), (3, 2), (2, 3), (1, 4)]
guarda un listado de tuplas con el eslora del barco y el número que hay que dibujar

#### BARCO_CHAR= "1"
representa el barco

#### AGUA_CHAR = "~"
representa el agua

#### TOCADO_CHAR = "X"
representa un tocado de barco

#### FALLO_CHAR = "Ø"
representa un disparo en el agiua
