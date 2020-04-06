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
