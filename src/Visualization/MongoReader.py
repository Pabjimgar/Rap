from pymongo import MongoClient

client = MongoClient("localhost", 27017)
database = client["MusicStats"]


def read_from_mongo(estilo, artista, column_name="text_no_sw"):

    """Function designed to read a dictionary from mongo"""
    collection = database[estilo]
    return collection.find_one({"_id": artista})[column_name]
