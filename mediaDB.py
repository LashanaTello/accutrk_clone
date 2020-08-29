from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime
from config import keys
from constants import MEDIA, MEDIA_LIST, CURRENT_MEDIA_CHECKOUTS, MEDIA_CHECKOUT_HISTORY


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

    # returns list of all media currently available
    @staticmethod
    def get_available_list():
        return MediaDatabase.DATABASE[MEDIA_LIST].find({"checked_out": False}, {"_id": 0})

    # returns list detailing every time a piece of media was ever checked out
    @staticmethod
    def get_checkout_history():
        return MediaDatabase.DATABASE[MEDIA_CHECKOUT_HISTORY].find({}, {"_id": 0})

    # returns true if media was added to database, returns false otherwise
    @staticmethod
    def add_media(new_media):
        found_doc = MediaDatabase.DATABASE[MEDIA_LIST].find_one({"media_barcode": new_media["media_barcode"],
                                                                 "media_title": new_media["media_title"],
                                                                 "media_type": new_media["media_type"]})
        if found_doc is None:
            result = MediaDatabase.DATABASE[MEDIA_LIST].insert_one({"media_barcode": new_media["media_barcode"],
                                                                    "media_title": new_media["media_title"],
                                                                    "media_type": new_media["media_type"],
                                                                    "checked_out": False})
            if result.inserted_id is not None:
                return True
        return False

    # returns true if media was deleted from database, returns false otherwise
    @staticmethod
    def remove_media(media):
        result = MediaDatabase.DATABASE[MEDIA_LIST].delete_one({"media_barcode": media["media_barcode"],
                                                                "media_title": media["media_title"],
                                                                "media_type": media["media_type"]})

        if result.deleted_count > 0:
            return True
        return False

    # returns true if original_media is replaced with edited_media in the database, returns false otherwise
    @staticmethod
    def edit_media(original_media, edited_media):
        result = MediaDatabase.DATABASE[MEDIA_LIST].update_one({"media_barcode": original_media["media_barcode"],
                                                                "media_title": original_media["media_title"],
                                                                "media_type": original_media["media_type"]},
                                                               {"$set": {"media_barcode": edited_media["media_barcode"],
                                                                         "media_title": edited_media["media_title"],
                                                                         "media_type": edited_media["media_type"]}})

        if result.modified_count > 0:
            return True
        return False

    # returns list of all media student currently has out
    @staticmethod
    def get_student_checkouts(student_id):
        if len(student_id) == 8:
            student_check_outs = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find({"eid": student_id}, {"_id": 0})
        else:
            student_check_outs = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find({"barcode": student_id},
                                                                                      {"_id": 0})
        return student_check_outs

    # reads user media input and determines whether to check media in or out based on the user input
    @staticmethod
    def evaluate_media_input(media_barcode):
        # check if media_barcode exists in MEDIA_LIST collection
        wanted_media = MediaDatabase.DATABASE[MEDIA_LIST].find_one({"media_barcode": media_barcode}, {"_id": 0})
        if wanted_media is None:
            return False

        # check if wanted_media is currently checked out
        result = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find_one({"media_barcode": media_barcode}, {"_id": 0})

        if result is None:
            return "out", wanted_media
        else:
            student_check_outs = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find(
                {"$or": [{"eid": result["eid"]}, {"barcode": result["barcode"]}]}, {"_id": 0})
            return "in", result, student_check_outs

    # checks out media under student represented by student_info, meaning the media is in the student's possession
    # returns true if media was checked out by the student, returns false otherwise
    @staticmethod
    def check_out(media, student_info):
        result = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].insert_one(
            {"media_barcode": media["media_barcode"],
             "media_title": media["media_title"],
             "media_type": media["media_type"],
             "eid": student_info["eid"],
             "barcode": student_info["barcode"],
             "first_name": student_info["first_name"],
             "last_name": student_info["last_name"],
             "check_out_time": datetime.datetime.utcnow(),
             "check_in_time": ""})

        if result.inserted_id is not None:
            update = MediaDatabase.DATABASE[MEDIA_LIST].update_one({"media_barcode": media["media_barcode"]},
                                                                   {"$set": {"checked_out": True}})
            if update.modified_count > 0:
                return True
        return False

    # checks in media that was borrowed by a student
    # returns true if media was successfully removed from the current media checkout collection and its entry was moved
    # to the checkout history collection
    @staticmethod
    def check_in(media_barcode):
        check_out_entry = MediaDatabase.DATABASE[CURRENT_MEDIA_CHECKOUTS].find_one_and_delete(
            {"media_barcode": media_barcode})
        update = MediaDatabase.DATABASE[MEDIA_LIST].update_one({"media_barcode": media_barcode},
                                                               {"$set": {"checked_out": False}})

        check_out_entry["check_in_time"] = datetime.datetime.utcnow()
        result = MediaDatabase.DATABASE[MEDIA_CHECKOUT_HISTORY].insert_one(check_out_entry)
        if result.inserted_id is not None:
            if update.modified_count > 0:
                return True
        return False
