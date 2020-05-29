from nltk.corpus import stopwords
import unidecode

stop_words = set(stopwords.words('spanish'))
extra_stop_words = ["estribillo", "bis", "x2", "x3", "x4", "x5", "k", "coros", "", " ", "q", "...", "pa", "ye", "oh",
                    "si", "se", "tan", "ay", "na", "lere", "ke", "paparapapapa", "parapapa", "you", "i", "the", "ma",
                    "on", "to", "ah", "eh", "d", "x", "to", "er", "aja", "cheik", "?que", "tralara", "yee", "uuuu",
                    "we", "it", "and"
                    ]


def remove_stopwords(iterable, invalid_words=stop_words):
    """Función diseñada para eliminar palabras que no queremos que formen parte del análisis"""

    for word in extra_stop_words:
        invalid_words.add(word)

    iterable_lower = [word.lower() for word in iterable if word.lower() not in invalid_words]
    result = [unidecode.unidecode(word) for word in iterable_lower]
    return result
