import string
from nltk.corpus import stopwords

# no se si deberíamos también bajar las de inglés
stopwords_espanol = stopwords.words("spanish")
stopwords_ingles = stopwords.words("english")


def limpiaTexto(prompt: str) -> set:
    # eliminación de puntuación y números y pase a minúsculas
    prompt = prompt.translate(str.maketrans("", "", string.punctuation)).lower()
    # separación de palabras
    palabras = set(prompt.split(" "))
    res = [
        p for p in palabras if p not in stopwords_espanol and p not in stopwords_ingles
    ]
    return res
