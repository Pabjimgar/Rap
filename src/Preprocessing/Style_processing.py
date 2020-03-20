

def consolidate_style(collection, estilo, collection_to_save):

    total_number_of_songs = 0
    total_number_of_artists = 0
    total_number_of_words = []
    relevant_words = []
    lengths = []

    for doc in collection.find():
        total_number_of_songs += doc["number_of_songs"]
        total_number_of_words.extend(doc["text_raw"])
        relevant_words.extend((doc["text_no_sw"]))
        total_number_of_artists += 1
        lengths.append(doc["max_words_per_song"])
        lengths.append(doc["min_words_per_song"])

    final_dictionary = {
                "_id": estilo,
                "text_no_sw": relevant_words,
                "unique_words": list(set(relevant_words)),
                "number_of_songs": total_number_of_songs,
                "word_average_per_song": len(total_number_of_words)/total_number_of_songs,
                "max_words_per_song": max(lengths),
                "min_words_per_song": min(lengths)
            }

    collection_to_save.insert(final_dictionary)