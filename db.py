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
        Database.DATABASE["students"].insert(student)

    # returns list of all students
    @staticmethod
    def get_all_students():
        return Database.DATABASE["students"].find({}, {"_id": 0})

    # changes last name of student whose eid is an_eid
    # not finished making this yet
    @staticmethod
    def update_student_last_name(an_eid, new_last_name):
        Database.DATABASE["students"].update_one({"eid": an_eid}, { "$set": {"last_name": new_last_name} })



