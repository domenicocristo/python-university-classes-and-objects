"""
Scrivete una funzione di nome disegna_rett che prenda un oggetto Turtle e un 
Rettangolo e usi la Tartaruga per disegnare il Rettangolo.

Scrivete una funzione di nome disegna_cerchio che prenda un oggetto Turtle e un Cerchio,
e disegni il Cerchio.
"""

import turtle
import math

class Rettangolo:
    def __init__(self, x, y, larghezza, altezza):
        self.x = x
        self.y = y
        self.larghezza = larghezza
        self.altezza = altezza

class Cerchio:
    def __init__(self, x, y, raggio):
        self.x = x
        self.y = y
        self.raggio = raggio

def disegna_rett(t, rettangolo):
    # Disegna un rettangolo utilizzando un oggetto Turtle
    t.penup()
    t.goto(rettangolo.x, rettangolo.y)
    t.setheading(0)  # orienta la tartaruga verso destra
    t.pendown()
    for i in range(2):
        t.forward(rettangolo.larghezza)
        t.left(90)
        t.forward(rettangolo.altezza)
        t.left(90)

def disegna_cerchio(t, cerchio):
    # Disegna un cerchio utilizzando un oggetto Turtle
    t.penup()
    t.goto(cerchio.x, cerchio.y)
    t.pendown()
    circonferenza = 2 * math.pi * cerchio.raggio
    lato = circonferenza / 360  # calcola la lunghezza del lato
    for i in range(360):
        t.forward(lato)
        t.left(1)

# Crea un oggetto Turtle
t = turtle.Turtle()

# Crea un oggetto Rettangolo con coordinate (0, 0), larghezza 100 e altezza 50
rettangolo = Rettangolo(0, 0, 100, 50)

# Disegna il rettangolo utilizzando la funzione disegna_rett
disegna_rett(t, rettangolo)

# Crea un oggetto Cerchio con coordinate (0, 0) e raggio 50
cerchio = Cerchio(0, 0, 50)

# Disegna il cerchio utilizzando la funzione disegna_cerchio
disegna_cerchio(t, cerchio)