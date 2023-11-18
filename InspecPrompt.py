from nltk.corpus import stopwords
import string

stopwords_espanol = stopwords.words("spanish")
stopwords_ingles = stopwords.words("english")


class Analizador:
    def __init__(self):
        self.secuencias = {}

    def limpiaTexto(self, prompt: str) -> list:
        # elimino comas, dos puntos y punto y comas
        prompt = prompt.translate(str.maketrans("", "", ",:;"))
        # eliminación de acentos
        prompt = prompt.translate(str.maketrans("áéíóú", "aeiou"))
        # pase a minúsculas y separacion
        prompt = prompt.lower().split(" ")
        # edepuración de stopwords
        res = [
            p
            for p in prompt
            if p not in stopwords_espanol and p not in stopwords_ingles
        ]
        return res

    def insertaTrigger(self, origen, destino, peso=None):
        if origen not in self.secuencias:
            self.secuencias[origen] = {}
        if destino not in self.secuencias:
            self.secuencias[destino] = {}
        self.secuencias[origen][destino] = peso

    def insertaSecuenciaDeTriggers(self, cadena: str):
        palabras = self.limpiaTexto(cadena)
        previo = palabras.pop(0)
        for p in palabras:
            self.insertaTrigger(previo, p)
            previo = p

    def encontrarDatosSensibles(self, word: str) -> bool:
        """Función que busca determinar si la secuencia de caracteres otorgada es una secuencia
        sensible/peligrosa y regresa un booleano."""
        danger = 0
        flag = False
        if word.isdigit() == True:
            if len(word) > 9 or len(word) <= 12:
                danger += 5
        else:
            if len(word) >= 10:
                danger += 1
            for c in word:
                if c in string.punctuation:
                    danger += 2
                if c.isupper():
                    danger += 2
                if c == "@":
                    flag = True
                if c == "." and flag == True:
                    danger += 5
                if c.isdigit():
                    danger += 2
        return danger >= 5

    def analiza_vulnerabilidad_de_prompt(self, prompt: list) -> [int, int]:
        palabras = self.limpiaTexto(prompt)
        susis = 0
        secsAlCuad = 0
        secActual = 0
        previo = ""
        for p in palabras:
            if p.isdigit() and len(p) < 8 or len(p) > 12:
                p = "unnumero"
            # reviso si la secuencia de la anterior con la actual está fichada como vulnerable
            if previo in self.secuencias and p in self.secuencias[previo]:
                secActual += 1
            else:
                secsAlCuad += secActual**2
                secActual = 0
                if self.encontrarDatosSensibles(p):
                    susis += 1
            previo = p
        secsAlCuad += secActual**2
        return susis, secsAlCuad

    def veredicto(self, query: str):
        notoriedades, secuencias = self.analiza_vulnerabilidad_de_prompt(query)
        """_description_
        Regresa un mensaje que indica el riesgo de seguridad de la entrada. El riesgo de seguridad se calcula con base en
        dos valores: secuencias y notoriedades. secuencias es un valor entre 0 y 100 que indica el riesgo de seguridad de la entrada. notoriedades es
        un valor entre 0 y 5 que indica el riesgo de seguridad de la entrada. Si notoriedades es mayor o igual a 4, la entrada
        presenta un alto riesgo de seguridad. Si notoriedades es 3, la entrada presenta un riesgo de seguridad. Si notoriedades es menor
        o igual a 0, la entrada presenta un bajo riesgo de seguridad. Si notoriedades es mayor o igual a 1 y menor o igual a 2,
        se evalúa el valor de secuencias. Si secuencias es mayor o igual a 50, la entrada presenta un alto riesgo de seguridad. Si secuencias es
        menor o igual a 25, la entrada presenta un riesgo de seguridad. Si secuencias es mayor a 25 y menor a 50, la entrada
        presenta un bajo riesgo de seguridad.
        Args:
            secuencias (int): Un valor entre 0 y 100 que indica el riesgo de seguridad de la entrada.
            notoriedades (int): Un valor entre 0 y 5 que indica el riesgo de seguridad de la entrada.

        Returns:
            str: Un mensaje que indica el riesgo de seguridad de la entrada.
        """

        if notoriedades >= 4 or secuencias >= 50:
            return "La consulta presenta un alto riesgo de seguridad, debe modificarse."
        elif notoriedades >= 2 or secuencias >= 25:
            return "La consulta podría contener información sensible."
        else:
            return "La consulta puede proceder."
