import sensibleData
import InspecPrompt


class Grafo:
    def __init__(self):
        self.G = {}

    def inserta(self, origen, destino, peso=None):
        if origen not in self.G:
            self.G[origen] = {}
        if destino not in self.G:
            self.G[destino] = {}
        self.G[origen][destino] = peso

    def multiInserta(self, cadena: str):
        palabras = InspecPrompt.limpiaTexto(cadena)
        previo = palabras.pop(0)
        for p in palabras:
            self.inserta(previo, p)
            previo = p


peligro = Grafo()
peligro.inserta("cuenta", "bancaria")
peligro.inserta("banco", "unnumero")
peligro.inserta("bancaria", "unnumero")
peligro.inserta("clave", "unnumero")
peligro.inserta("usuario", "unnumero")
peligro.inserta("contraseña", "unnumero")


def analiza_vulnerabilidad(palabras: list) -> [int, int]:
    susis = 0
    secsAlCuad = 0
    secActual = 0
    previo = ""
    for p in palabras:
        if p.isdigit() and len(p) < 8 or len(p) > 12:
            p = "unnumero"
        # reviso si la secuencia de la anterior con la actual está fichada como vulnerable
        if previo in peligro.G and p in peligro.G[previo]:
            secActual += 1
        else:
            secsAlCuad += secActual**2
            secActual = 0
            if sensibleData.encontrarDatosSensibles(p):
                susis += 1
        previo = p
    return susis, secsAlCuad
