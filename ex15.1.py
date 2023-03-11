"""
Scrivete una definizione di classe di nome Cerchio, avente gli attributi centro e 
raggio, dove centro è un oggetto Punto e raggio è un numero.

Istanziate un oggetto Cerchio che rappresenti un cerchio con il centro nel punto (150, 100)
e di raggio 75.

Scrivete una funzione di nome punto_nel_cerchio, che prenda un Cerchio e un Punto e 
restituisca True se il punto giace dentro il cerchio, circonferenza compresa.

Scrivete una funzione di nome rett_nel_cerchio, che prenda un Cerchio e un Rettangolo e 
e restituisca True se il rettangolo giace interamente all'interno del cerchio, circonferenza compresa.

Scrivete una funzione di nome rett_cerchio_sovrapp, che prenda un Cerchio e un Rettangolo 
e restituisca True se almeno uno degli angoli del Rettangolo ricade all'interno del cerchio. 
Oppure, più difficile, se una qualunque porzione del Rettangolo ricade all'interno del cerchio.
"""

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cerchio:
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio

class Rettangolo:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

def punto_nel_cerchio(cerchio, punto):
    distanza = math.sqrt((punto.x - cerchio.centro.x)**2 + (punto.y - cerchio.centro.y)**2)
    return distanza <= cerchio.raggio

def rett_nel_cerchio(cerchio, rettangolo):
    # Calcoliamo la coordinata x del centro del rettangolo
    centro_x = (rettangolo.x_min + rettangolo.x_max) / 2
    # Calcoliamo la coordinata y del centro del rettangolo
    centro_y = (rettangolo.y_min + rettangolo.y_max) / 2
    # Creiamo un oggetto Punto che rappresenta il centro del rettangolo
    centro_rettangolo = Punto(centro_x, centro_y)
    # Verifichiamo se il centro del rettangolo giace dentro il cerchio
    if not punto_nel_cerchio(cerchio, centro_rettangolo):
        return False
    # Verifichiamo se i vertici del rettangolo giacciono tutti dentro il cerchio
    if not punto_nel_cerchio(cerchio, Punto(rettangolo.x_min, rettangolo.y_min)):
        return False
    if not punto_nel_cerchio(cerchio, Punto(rettangolo.x_min, rettangolo.y_max)):
        return False
    if not punto_nel_cerchio(cerchio, Punto(rettangolo.x_max, rettangolo.y_min)):
        return False
    if not punto_nel_cerchio(cerchio, Punto(rettangolo.x_max, rettangolo.y_max)):
        return False
    # Se tutti i vertici del rettangolo giacciono dentro il cerchio, restituiamo True
    return True

def rett_cerchio_sovrapp(cerchio, rettangolo):
    # Verifichiamo se il centro del rettangolo giace dentro il cerchio
    centro_x = (rettangolo.x_min + rettangolo.x_max) / 2
    centro_y = (rettangolo.y_min + rettangolo.y_max) / 2
    if punto_nel_cerchio(cerchio, Punto(centro_x, centro_y)):
        return True
    # Verifichiamo se i lati del rettangolo si intersecano con il cerchio
    if (rettangolo.x_min <= cerchio.centro.x + cerchio.raggio and
        rettangolo.x_max >= cerchio.centro.x - cerchio.raggio and
        rettangolo.y_min <= cerchio.centro.y + cerchio.raggio and
        rettangolo.y_max >= cerchio.centro.y - cerchio.raggio):
        return True
    return False

cerchio = Cerchio(Punto(0, 0), 5)
punto1 = Punto(4, 0)
punto2 = Punto(6, 0)

print(punto_nel_cerchio(cerchio, punto1))  # True
print(punto_nel_cerchio(cerchio, punto2))  # False

rettangolo1 = Rettangolo(-2, -2, 2, 2)
rettangolo2 = Rettangolo(-6, -6, -4, -4)

print(rett_nel_cerchio(cerchio, rettangolo1))  # True
print(rett_nel_cerchio(cerchio, rettangolo2))  # False

rettangolo3 = Rettangolo(-4,-4,4,4)
rettangolo4 = Rettangolo(-6,-6,-4,-4)
rettangolo5 = Rettangolo(-6,-6,-7,-7)

print(rett_cerchio_sovrapp(cerchio, rettangolo3)) # True
print(rett_cerchio_sovrapp(cerchio, rettangolo4)) # True
print(rett_cerchio_sovrapp(cerchio, rettangolo5)) # False