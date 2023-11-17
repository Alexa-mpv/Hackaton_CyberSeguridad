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
