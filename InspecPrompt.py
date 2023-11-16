import nltk
import string

nltk.download("stopwords")
from nltk.corpus import stopwords

# no se si deberíamos también bajar las de inglés
stopwords_espanol = stopwords.words("spanish")


def limpiaTexto(prompt: str) -> list:
    # eliminación de puntuación y números y pase a minúsculas
    prompt = prompt.translate(str.maketrans("", "", string.punctuation)).lower()
    # separación de palabras
    palabras = prompt.split(" ")
    res = [p for p in palabras if p not in stopwords_espanol]
    return res
