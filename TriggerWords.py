import sensibleData
import requests


class Grafo:
    def __init__(self):
        self.G = {}

    def inserta(self, origen, destino, peso=None):
        if origen not in self.G:
            self.G[origen] = {}
        if destino not in self.G:
            self.G[destino] = {}
        self.G[origen][destino] = peso


peligro = Grafo()
peligro.inserta()


def analiza_vulnerabilidad(palabras: list) -> [int, int]:
    susis = 0
    secsAlCuad = 0
    secActual = 0
    previo = ""
    esNum = False
    for p in palabras:
        # reviso si la secuencia de la anterior con la actual está fichada como vulnerable
        if p.isdigit():
            p = "aNumber"
        if p in peligro.G[previo]:
            secActual += 1
        else:
            secsAlCuad += secActual**2
            secActual = 0
            if sensibleData.encontrarDatosSensibles(p):
                susis += 1
        previo = p
    return susis, secsAlCuad
