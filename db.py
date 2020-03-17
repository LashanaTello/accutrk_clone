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
    # ##########################change this
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

    # Classes page methods

    # adds a class whose "subject" is subject, "catalog" is catalog, "section" is section and "professor" is professor
    # catalog defaults to "99999" and section defaults to "99" if neither is provided
    # professor defaults to an empty dictionary if no professor is provided
    # returns true if class was successfully added and returns false otherwise
    @staticmethod
    def add_class(subject, catalog="99999", section="99", professor={}):
        found_doc = Database.DATABASE["classes"].find_one({"subject": subject, "catalog": catalog, "section": section})
        if found_doc is None:
            class_roster = []
            Database.DATABASE["classes"].insert_one({"subject": subject, "catalog": catalog, "section": section,
                                                     "professor": professor, "class_roster": class_roster})
            return True
        return False

    # returns list of all classes in the system
    @staticmethod
    def get_all_classes():
        return Database.DATABASE["classes"].find({}, {"_id": 0})

    # changes the subject of the class whose subject, catalog, and section fields match the given parameters
    # the class's subject field will be set to new_subject
    # returns true if class's subject is changed to new_subject and returns false otherwise
    @staticmethod
    def update_class_subject(new_subject, subject, catalog, section):
        result = Database.DATABASE["classes"].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                         {"$set": {"subject": new_subject}})
        if result.modified_count > 0:
            return True
        return False

    # changes the catalog of the class whose subject, catalog, and section fields match the given parameters
    # the class's catalog field will be set to new_catalog
    # returns true if class's catalog is changed to new_catalog and returns false otherwise
    @staticmethod
    def update_class_catalog(new_catalog, subject, catalog, section):
        result = Database.DATABASE["classes"].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                         {"$set": {"catalog": new_catalog}})
        if result.modified_count > 0:
            return True
        return False

    # changes the section of the class whose subject, catalog, and section fields match the given parameters
    # the class's section field will be set to new_section
    # returns true if class's section is changed to new_section and returns false otherwise
    @staticmethod
    def update_class_section(new_section, subject, catalog, section):
        result = Database.DATABASE["classes"].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                         {"$set": {"section": new_section}})
        if result.modified_count > 0:
            return True
        return False

    # changes the professor of the class whose subject, catalog, and section fields match the given parameters
    # the first_name and last_name field of the class's professor field will be set to prof_first_name and
    # prof_last_name, respectively
    # returns true if class's professor is changed and returns false otherwise
    @staticmethod
    def update_class_professor(prof_first_name, prof_last_name, email, subject, catalog, section):
        result = Database.DATABASE["classes"].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                         {"$set": {"professor.first_name": prof_first_name,
                                                                   "professor.last_name": prof_last_name,
                                                                   "email": email}})
        if result.modified_count > 0:
            return True
        return False

    # deletes class whose subject, catalog and section match the given parameters from system
    # returns true if class was deleted and returns false otherwise
    @staticmethod
    def remove_class(subject, catalog, section):
        result = Database.DATABASE["classes"].delete_one({"subject": subject, "catalog": catalog, "section": section})
        if result.deleted_count > 0:
            return True
        return False

    # professors page

    # adds professor to system
    # returns true if professor was added, returns false otherwise
    @staticmethod
    def add_professor(first_name, last_name, email):
        found_doc = Database.DATABASE["professors"].find_one({"first_name": first_name,
                                                              "last_name": last_name, "email": email})
        if found_doc is None:
            Database.DATABASE["professors"].insert_one(
                {"first_name": first_name, "last_name": last_name, "email": email})
            return True
        return False

    # register page
