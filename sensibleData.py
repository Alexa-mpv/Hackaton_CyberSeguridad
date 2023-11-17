import string
import TriggerWords


def encontrarDatosSensibles(word):
    """Función que busca determinar si la secuencia de caracteres otorgada es una secuencia
    sensible/peligrosa y regresa un booleano."""

    danger = 0

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


print(encontrarDatosSensibles("hola"))
print(encontrarDatosSensibles("hola123"))
print(encontrarDatosSensibles("hola123@"))
print(encontrarDatosSensibles("123456789123"))
print(encontrarDatosSensibles("Alexa"))
print(encontrarDatosSensibles("ALEXA"))


def analiza_vulnerabilidad_de_prompt(
    palabras: list, triggersGraph: TriggerWords.Grafo
) -> [int, int]:
    susis = 0
    secsAlCuad = 0
    secActual = 0
    previo = ""
    for p in palabras:
        if p.isdigit() and len(p) < 8 or len(p) > 12:
            p = "unnumero"
        # reviso si la secuencia de la anterior con la actual está fichada como vulnerable
        if previo in triggersGraph.G and p in triggersGraph.G[previo]:
            secActual += 1
        else:
            secsAlCuad += secActual**2
            secActual = 0
            if encontrarDatosSensibles(p):
                susis += 1
        previo = p
    return susis, secsAlCuad
