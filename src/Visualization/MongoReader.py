from pymongo import MongoClient

client = MongoClient("localhost", 27017)
database = client["rapstats"]
collection = database["artists_raw"]


def read_from_mongo(artist_name, column_name="text_no_sw"):

    """Function designed to read a dictionary from mongo"""

    return collection.find_one({"_id": artist_name})[column_name]
