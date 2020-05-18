from pymongo import MongoClient
from Preprocessing import Counting_class, Spanish_corpus
from Preprocessing.Tags import DbTags
import string

CLIENT = MongoClient("localhost", 27017)
DATABASE = CLIENT["MusicStats"]


def set_style_collection(estilo):
    return DATABASE[estilo]


def set_database():
    return DATABASE


def read_artist_from_mongo(estilo, artista, column_name="text_no_sw"):

    """Function designed to read a dictionary from mongo"""
    collection = DATABASE[estilo]
    return collection.find_one({"_id": artista})[column_name]


def file_to_mongo(file_path, artist_name, estilo, n_albums=1):

    """Function designed to save a file with all the words counted under an artist name"""

    with open(file_path, "r") as file:

        reader = file.read()

        split_file = reader.split()

        length_list = []
        for song in reader.split("\n")[:-1]:
            length_list.append(len(song.split(" ")))

        max_song, min_song = (max(length_list), min(length_list))

        no_punctuation_file = ["".join(caracter for caracter in word if caracter
                                       not in string.punctuation) for word in split_file]

        number_of_songs = len(reader.split("\n")) - 1

        word_average_per_song = Counting_class.calculate_average_per_song(no_punctuation_file, number_of_songs)

        counted_dictionary_raw = len(no_punctuation_file)

        dictionary_no_sw = Spanish_corpus.remove_stopwords(no_punctuation_file)
        unique_words = list(set(dictionary_no_sw))
        num_of_relevant_words = len(dictionary_no_sw)
        number_of_stopwords = counted_dictionary_raw - num_of_relevant_words
        percentage = num_of_relevant_words / counted_dictionary_raw * 100

        tags = DbTags

        # Aqui guardamos el objeto que más tardaré registraremos en mongo
        final_dictionary = {
            tags.id: artist_name,
            tags.text_raw: no_punctuation_file,
            tags.text_no_sw: dictionary_no_sw,
            tags.unique_words: unique_words,
            tags.number_of_songs: number_of_songs,
            tags.word_average_per_song: word_average_per_song,
            tags.number_of_stopwords: number_of_stopwords,
            tags.percentage_of_relevant_words: percentage,
            tags.max_words_per_song: max_song,
            tags.min_words_per_song: min_song,
            tags.number_of_albums: n_albums
        }

        set_style_collection(estilo).insert(final_dictionary)
