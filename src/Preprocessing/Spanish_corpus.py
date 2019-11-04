from nltk.corpus import stopwords
import unidecode
from collections import Counter


stop_words = set(stopwords.words('spanish'))


def remove_stopwords(iterable, invalid_words=stop_words):

    iterable_lower = [word.lower() for word in iterable if word.lower() not in invalid_words]
    prueba = [unidecode.unidecode(word) for word in iterable_lower]
    return prueba
