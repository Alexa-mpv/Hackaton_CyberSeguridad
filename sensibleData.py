import re
import string


def encontrarDatosSensibles(word):
    """Función que busca determinar si la secuencia de caracteres otorgada es una secuencia
    sensible/peligrosa y regresa un booleano."""

    danger = 0
    num = 0

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
