from Preprocessing import Database_ops
from Preprocessing.Tags import Tags


def consolidate_style(collection, estilo, collection_to_save):

    tags = Tags

    total_number_of_songs = 0
    total_number_of_artists = 0
    total_number_of_albums = 0
    total_number_of_words = []
    relevant_words = []
    lengths = []

    for doc in collection.find():
        total_number_of_songs += doc[tags.number_of_songs]
        total_number_of_words.extend(doc[tags.text_raw])
        relevant_words.extend((doc[tags.text_no_sw]))
        total_number_of_artists += 1
        total_number_of_albums += int(doc[tags.number_of_albums])
        lengths.append(doc[tags.max_words_per_song])
        lengths.append(doc[tags.min_words_per_song])

    final_dictionary = {
                tags.id: estilo,
                tags.text_raw: total_number_of_words,
                tags.text_no_sw: relevant_words,
                tags.unique_words: list(set(relevant_words)),
                tags.number_of_songs: total_number_of_songs,
                tags.word_average_per_song: len(total_number_of_words)/total_number_of_songs,
                tags.max_words_per_song: max(lengths),
                tags.min_words_per_song: min(lengths),
                tags.number_of_albums: total_number_of_albums
            }

    if collection.name == collection_to_save:
        Database_ops.set_style_collection(collection_to_save).insert(final_dictionary)
    else:
        Database_ops.set_style_collection(estilo).insert(final_dictionary)
        Database_ops.set_style_collection(collection_to_save).insert(final_dictionary)
