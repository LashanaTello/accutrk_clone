from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import keys, defaultDB


class Database(object):
    uri = keys.mongoURI
    DATABASE = None

    @staticmethod
    def initialize():
        try:
            client = MongoClient(Database.uri)
            Database.DATABASE = client[defaultDB.dbName]
            print("Successfully connected to db")
        except ConnectionFailure:
            print("Couldn't connect to database")
        except:
            print("Something went wrong")

    # main page methods

    # returns list of all students currently logged in
    @staticmethod
    def list_all_logins():
        return Database.DATABASE["current_logins"].find()

    # students page methods

    # adds a student to database
    @staticmethod
    def add_student(student):
        found_doc = Database.DATABASE["students"].find({"eid": student["eid"]})
        if found_doc is None:
            Database.DATABASE["students"].insert_one(student)
            return True
        return False

    # returns list of all students
    @staticmethod
    def get_all_students():
        return Database.DATABASE["students"].find({}, {"_id": 0})

    # changes last name of student whose eid is an_eid
    @staticmethod
    def update_student_last_name(an_eid, new_last_name):
        Database.DATABASE["students"].update_one({"eid": an_eid}, {"$set": {"last_name": new_last_name}})

    # changes first name of student whose eid is an_eid
    @staticmethod
    def update_student_first_name(an_eid, new_first_name):
        Database.DATABASE["students"].update_one({"eid": an_eid}, {"$set": {"first_name": new_first_name}})

    # changes email of student whose eid is an_eid
    @staticmethod
    def update_student_email(an_eid, new_email):
        Database.DATABASE["students"].update_one({"eid": an_eid}, {"$set": {"email": new_email}})

    # changes barcode of student whose eid is an_eid
    @staticmethod
    def update_student_barcode(an_eid, new_barcode):
        Database.DATABASE["students"].update_one({"eid": an_eid}, {"$set": {"barcode": new_barcode}})

    # changes eid of student whose eid is an_eid
    @staticmethod
    def update_student_eid(an_eid, new_eid):
        Database.DATABASE["students"].update_one({"eid": an_eid}, {"$set": {"eid": new_eid}})

    # removes student whose eid is an_eid from system
    @staticmethod
    def remove_student(an_eid):
        Database.DATABASE["students"].delete_one({"eid": an_eid})
