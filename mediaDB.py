from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime
from config import keys
from constants import MEDIA
from constants import MEDIA_LIST
from constants import CURRENT_MEDIA_CHECKOUTS
from constants import MEDIA_CHECKOUT_HISTORY


class MediaDatabase(object):
    uri = keys.mongoURI
    DATABASE = None

    @staticmethod
    def initialize():
        try:
            client = MongoClient(MediaDatabase.uri)
            MediaDatabase.DATABASE = client[MEDIA]
            print("Successfully connected to media db")
        except ConnectionFailure:
            print("Couldn't connect to media database")
        except:
            print("Something went wrong")

    # returns list of all media in the database
    @staticmethod
    def get_all_media():
        return MediaDatabase.DATABASE[MEDIA_LIST].find({}, {"_id": 0})

    # returns list of all media currently checked out
    @staticmethod
    def get_checkout_list():
        return MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find({}, {"_id": 0})

    # returns list detailing every time a piece of media was ever checked out
    @staticmethod
    def get_checkout_history():
        return MediaDatabase.DATABASE[MEDIA_CHECKOUT_HISTORY].find({}, {"_id": 0})

    # returns true if media was added to database, returns false otherwise
    @staticmethod
    def add_media(new_media):
        result = MediaDatabase.DATABASE[MEDIA_LIST].update_one({"media_barcode": new_media["media_barcode"],
                                                                "media_title": new_media["media_title"],
                                                                "media_type": new_media["media_type"]},
                                                               {"$set":
                                                                    {"media_barcode": new_media["media_barcode"],
                                                                     "media_title": new_media["media_title"],
                                                                     "media_type": new_media["media_type"]}},
                                                               upsert=True)

        if result.upserted_id is not None:
            return True
        return False
