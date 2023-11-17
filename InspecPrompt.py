import string
from nltk.corpus import stopwords

stopwords_espanol = stopwords.words("spanish")
stopwords_ingles = stopwords.words("english")


def limpiaTexto(prompt: str) -> list:
    # eliminación de puntuación y números y pase a minúsculas
    prompt = prompt.translate(str.maketrans("", "", string.punctuation)).lower()
    # separación de palabras
    palabras = set(prompt.split(" "))
    res = [
        p for p in palabras if p not in stopwords_espanol and p not in stopwords_ingles
    ]
    return res


print(
    limpiaTexto(
        "Este en un prompt bien fachero sin información sensible definitivamente, en serio. Tengo 2 vacas."
    )
)