import csv
from datetime import date, datetime
from . import FICHERO



class Movimiento():
    def __init__(self, diccionario):
        try:
            self.fecha = date.fromisoformat(diccionario['fecha'])

            ahora = datetime.now()
            if self.fecha.strftime("%Y%m%d")  > ahora.strftime("%Y%m%d"):
                raise self.errores.append("La fecha no puede ser superior a la actual")

        except ValueError:
            raise self.errores.append("Formato de fecha incorrecto")


        self.concepto = diccionario['concepto']
        if self.concepto == "":
            raise self.errores.append("Informe el concepto")

        
        try:
            self.ingreso_gasto = diccionario['ingreso_gasto']
        except KeyError:
            raise self.errores.append("informe tipo de movimiento (Ingreso/Gasto)")
        
        try:
            self.cantidad = diccionario['cantidad']
            if self.cantidad <= 0:
                raise self.errores.append("Cantidad debe ser positiva.")
        except ValueError:
            raise self.errores.append("Cantidad debe ser un número.")





class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        fichero = open(FICHERO, "r", encoding="utf-8")
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()
    
    def escribir(self):
        if len(self.movimientos) == 0:
            return
        fichero = open(FICHERO, "w", encoding="utf-8")
        nombres_campo = list(self.movimientos[0].keys())
        dwriter = csv.DictWriter(fichero, fieldnames = nombres_campo)
        dwriter.writeheader()
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        fichero.close()

    def añadir(self, valor):
        movimiento = {}
        movimiento['fecha'] = valor['fecha']
        movimiento['concepto'] = valor['concepto']
        movimiento['ingreso_gasto'] = valor['ingreso_gasto']
        movimiento['cantidad'] = valor['cantidad']
        self.movimientos.append(movimiento)