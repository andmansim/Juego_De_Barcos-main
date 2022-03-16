from itertools import  product
from clases.Case import Case1
from clases.Barco import Barco1
from clases import Conventions

'''
from clases.Case import *
from clases.Barco import *
from Conventions import *
'''
class Tablero1:

  def __init__(self):
  # Creamos las casillas:
    case = Case1()
    case.generar_casillas()
    #generar_casillas()

    # Creamos los barcos:
    barco = Barco1()
    barco.generar_barcos()
    #generar_barcos()
    
    # performance / legibilidad:
    num_lineas = Conventions.tablero_num_lineas
    num_columnas = Conventions.tablero_num_columnas
    num2l = Conventions.generar_num_linea
    num2c = Conventions.generar_num_columna
    
    # Creamos la herramienta para poder seguir la situación
    self.casillas_jugadas = set()
    
    # Generamos aquí los etiquetas para facilitar la visualización
    self.etiqueta_lineas = [num2l(x) for x in range(num_lineas)]
    self.etiqueta_columnas = [num2c(x) for x in range(num_columnas)]
    
    trazo_horizontal = " --" + "+---" * 10 + "+"

  def ver(self):
    print("   |", " | ".join(self.etiqueta_columnas), "|")
    
    iter_etiqueta_lineas = iter(self.etiqueta_lineas)
    
    for x, y in product(range(Conventions.tablero_num_lineas),
                        range(Conventions.tablero_num_columnas)):
    
        # Trazo horizontal para cada nueva línea
        if y == 0:
            print(self.trazo_horizontal)
            print(" {}".format(next(iter_etiqueta_lineas)), end="")
    
        casilla = Case1.instances[x, y]
        print(" |", casilla, end="")
    
        # Ver la barra vertical derecha de la tabla:
        if y == 9:
            print(" |")
    # Ver la última línea horizontal
    print(self.trazo_horizontal + "\n\n")

