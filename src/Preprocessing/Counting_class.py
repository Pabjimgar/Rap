from collections import Counter


def count_total_number_of_words(file_path):
    """devuelve un Counter con todas las palabras del documento"""
    with open(file_path, "r") as file:
        return Counter(file.read().split())


def calculate_average_per_song(dictionary, number_of_songs):
    """Calcula la media de palabras por cancion"""
    return len(dictionary)/number_of_songs


def calculate_number_of_stopwords(dictionary_with_sw, dictionary_wo_sw):
    """Calcula el numero de stop words en un diccionario"""
    return len(dictionary_with_sw) - len(dictionary_wo_sw)
