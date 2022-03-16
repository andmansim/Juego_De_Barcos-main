from random import choices
import sys

from itertools import cycle, chain, product, repeat
from clases import Case
from clases import Conventions


HORIZONTAL = 0
VERTICAL = 1

ORIENTACIONES = (VERTICAL, HORIZONTAL)
instances = []
casillas_ocupadas = set()

class Barco1:
    def __init__(self, longitud):
            self.longitud = longitud
            self.orientacion = choices(ORIENTACIONES) #choice
            self.tocado = False
            self.hundido = False

            # performance / legibilidad:
            num_lineas = Conventions.tablero_num_lineas
            num_columnas = Conventions.tablero_num_columnas
            num2l = Conventions.generar_num_linea
            num2c = Conventions.generar_num_columna

            while True:
                if self.orientacion == HORIZONTAL:
                    rang = choices(range(num_lineas)) #choice
                    primero = choices(range(num_columnas + 1 - longitud)) #choice
                    letra = num2l(rang)
                    cifras = [num2c(x) for x in range(primero, primero + longitud)]
                    self.casillas = {Case.instances[l + c]
                                for l, c in product(repeat(letra, longitud), cifras)}
                else:
                    rang = choices(range(num_columnas)) #choice
                    primero = choices(range(num_lineas + 1 - longitud)) #choice
                    cifra = num2c(rang)
                    letras = [num2l(x) for x in range(primero, primero + longitud)]
                    # Crear el barco
                    self.casillas = {Case.instances[l + c]
                                for l, c in product(letras, repeat(cifra, longitud))}

                for existente in instances: #Barco.instances
                    if self.casillas.intersection(existente.casillas):
                        break  # break relativo al "for existente in barcos:"
                else:
                    # Agregar el barco en el contenedor de barcos
                    instances.append(self) #Barco.instances.append(self)
                    # Informar la casilla que contiene un barco.
                    for casilla in self.casillas:
                        casilla.barco = self
                    # Agregar estas casillas a las casillas ocupadas :
                    casillas_ocupadas |= self.casillas #Barco.casillas_ocupadas |= self.casillas
                    break  # break relativo al "while True:"

@classmethod
def generar_barcos(cls):
        for longitud in Conventions.barcos_longitud:
            Barco1(longitud) #Barco
