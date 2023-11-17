from nltk.corpus import stopwords

stopwords_espanol = stopwords.words("spanish")
stopwords_ingles = stopwords.words("english")


def limpiaTexto(prompt: str) -> list:
    # elimino comas, dos puntos y punto y comas
    prompt = prompt.translate(str.maketrans("", "", ",:;"))
    # eliminación de acentos
    prompt = prompt.translate(str.maketrans("áéíóú", "aeiou"))
    # pase a minúsculas y separacion
    prompt = prompt.lower().split(" ")
    # edepuración de stopwords
    res = [
        p for p in prompt if p not in stopwords_espanol and p not in stopwords_ingles
    ]
    return res


print(limpiaTexto("número telefónico unNumero"))
