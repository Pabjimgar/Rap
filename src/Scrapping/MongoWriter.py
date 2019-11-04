from pymongo import MongoClient
from Preprocessing import Counting_class
from Preprocessing import Spanish_corpus
import string


CLIENT = MongoClient("localhost", 27017)
DATABASE = CLIENT["rapstats"]
COLLECTION = DATABASE["artists_raw"]


def set_database(database_name):
    return CLIENT[database_name]


def set_collection(collection_name):
    return CLIENT[collection_name]


def insert_dictionary_into_collection(dictionary):

    COLLECTION.insert(dictionary)


def file_to_mongo(file_path, artist_name, estilo, pais):

    """Function designed to save a file with all the words counted under an artist name"""

    with open(file_path, "r") as file:

        reader = file.read()

        split_file = reader.split()

        no_punctuation_file = ["".join(caracter for caracter in word if caracter
                                       not in string.punctuation) for word in split_file]

        number_of_songs = len(reader.split("\n")) - 1

        word_average_per_song = Counting_class.calculate_average_per_song(no_punctuation_file, number_of_songs)

        counted_dictionary_raw = len(no_punctuation_file)
        counted_dictionary_no_sw = len(Spanish_corpus.remove_stopwords(no_punctuation_file))
        number_of_stopwords = counted_dictionary_raw - counted_dictionary_no_sw

        #Aqui guardamos el objeto que más tardaré registraremos en mongo
        final_dictionary = {
            "_id": artist_name,
            "text_raw": no_punctuation_file,
            "text_no_sw": counted_dictionary_no_sw,
            "number_of_songs": number_of_songs,
            "word_average_per_song": word_average_per_song,
            "number_of_stopwords": number_of_stopwords,
            "style": estilo,
            "country": pais,

        }

        insert_dictionary_into_collection(final_dictionary)