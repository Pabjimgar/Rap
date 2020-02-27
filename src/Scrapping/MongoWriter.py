from pymongo import MongoClient
from Preprocessing import Counting_class
from Preprocessing import Spanish_corpus
import string


CLIENT = MongoClient("localhost", 27017)
DATABASE = CLIENT["MusicStats"]


def set_style_collection(estilo):
    return DATABASE[estilo]


def set_database(database_name):
    return CLIENT[database_name]


def set_collection(collection_name):
    return CLIENT[collection_name]


def file_to_mongo(file_path, artist_name, estilo):

    """Function designed to save a file with all the words counted under an artist name"""

    with open(file_path, "r") as file:

        reader = file.read()

        split_file = reader.split()

        no_punctuation_file = ["".join(caracter for caracter in word if caracter
                                       not in string.punctuation) for word in split_file]

        number_of_songs = len(reader.split("\n")) - 1

        word_average_per_song = Counting_class.calculate_average_per_song(no_punctuation_file, number_of_songs)

        counted_dictionary_raw = len(no_punctuation_file)

        dictionary_no_sw = Spanish_corpus.remove_stopwords(no_punctuation_file)
        counted_dictionary_no_sw = len(dictionary_no_sw)
        number_of_stopwords = counted_dictionary_raw - counted_dictionary_no_sw
        percentage = counted_dictionary_no_sw / counted_dictionary_raw * 100

        # Aqui guardamos el objeto que más tardaré registraremos en mongo
        final_dictionary = {
            "_id": artist_name,
            "text_raw": no_punctuation_file,
            "text_no_sw": dictionary_no_sw,
            "number_of_songs": number_of_songs,
            "word_average_per_song": word_average_per_song,
            "number_of_stopwords": number_of_stopwords,
            "percentage_of_relevant_words": percentage
        }

        set_style_collection(estilo).insert(final_dictionary)