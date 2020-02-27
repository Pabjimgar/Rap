from nltk.corpus import stopwords
import unidecode
from collections import Counter


stop_words = set(stopwords.words('spanish'))
extra_stop_words = ["estribillo", "bis", "x2", "x3", "x4", "x5"]


def remove_stopwords(iterable, invalid_words=stop_words):

    for word in extra_stop_words:
        invalid_words.add(word)

    iterable_lower = [word.lower() for word in iterable if word.lower() not in invalid_words]
    prueba = [unidecode.unidecode(word) for word in iterable_lower]
    return prueba
