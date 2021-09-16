import csv
from . import FICHERO

# La clase movimiento no la usamos todavía

class Movimiento():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = es_ingreso
        self.cantidad = cantidad

class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        fichero = open(FICHERO, "r")
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()
    
    def escribir(self):
        if len(self.movimientos) == 0:
            return
        fichero = open(FICHERO, "w")
        nombres_campo = [self.movimientos[0].keys()]
        dreader = csv.DictWriter(fichero, fieldnames=nombres_campo)
        for movimiento in self.movimientos:
            dreader.writerow(movimiento)
        fichero.close()