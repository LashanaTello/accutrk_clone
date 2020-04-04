from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime
from config import keys, defaultDB
from constants import STUDENTS
from constants import CLASSES
from constants import PROFESSORS
from constants import CURRENT_LOGINS
from constants import LOGIN_HISTORY


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

    ####################################################################################################################
    #                                                main page methods
    ####################################################################################################################

    # returns list of all students currently logged in
    @staticmethod
    def list_all_logins():
        return Database.DATABASE[CURRENT_LOGINS].find({}, {"_id": 0})

    # -----------------------------------------     sign in/out process     --------------------------------------------

    # reads user input and determines whether to sign a student in or out based on the user input
    @staticmethod
    def evaluate_input(student_number):
        if len(student_number) == 8:
            result = Database.DATABASE[CURRENT_LOGINS].find_one({"eid": student_number}, {"_id": 0})
        else:
            result = Database.DATABASE[CURRENT_LOGINS].find_one({"barcode": student_number}, {"_id": 0})

        if result is None:
            return Database.get_info_for_sign_in(student_number)
        else:
            return Database.sign_out(student_number)

    # returns all student information for student whose eid or barcode matches student_number
    # the information returned contains the student's name, eid, barcode, and classes they're enrolled in
    @staticmethod
    def get_info_for_sign_in(student_number):
        if len(student_number) == 8:
            student_info = Database.DATABASE[STUDENTS].find_one({"eid": student_number},
                                                                {"_id": 0, "email": 0,
                                                                 "enrolled_list.registered_by": 0,
                                                                 "enrolled_list.registered_date": 0})
        else:
            student_info = Database.DATABASE[STUDENTS].find_one({"barcode": student_number},
                                                                {"_id": 0, "email": 0,
                                                                 "enrolled_list.registered_by": 0,
                                                                 "enrolled_list.registered_date": 0})

        return student_info

    # signs student in by adding them to the current_logins collection
    # also adds login entries to the login_history collection when doing manual sign-ins
    @staticmethod
    def sign_in(eid, barcode, first_name, last_name, subject, catalog, section, service, login_time="", logout_time=""):
        if login_time == "" and logout_time == "":
            login_time = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        if logout_time == "":
            result = Database.DATABASE[CURRENT_LOGINS].insert_one({"eid": eid, "barcode": barcode,
                                                                   "first_name": first_name, "last_name": last_name,
                                                                   "subject": subject, "catalog": catalog,
                                                                   "section": section, "login_time": login_time,
                                                                   "logout_time": logout_time, "service": service})
        else:
            result = Database.DATABASE[LOGIN_HISTORY].insert_one({"eid": eid, "barcode": barcode,
                                                                  "first_name": first_name, "last_name": last_name,
                                                                  "subject": subject, "catalog": catalog,
                                                                  "section": section, "login_time": login_time,
                                                                  "logout_time": logout_time, "service": service})

        if result.inserted_id is not None:
            return True
        return False

    # signs student in by adding them to the current_logins collection
    @staticmethod
    def signn_in(student):
        if student["login_time"] == "" and student["logout_time"] == "":
            student["login_time"] = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        if student["logout_time"] == "":
            result = Database.DATABASE[CURRENT_LOGINS].insert_one({"eid": student["eid"], "barcode": student["barcode"],
                                                                   "first_name": student["first_name"],
                                                                   "last_name": student["last_name"],
                                                                   "subject": student["subject"],
                                                                   "catalog": student["catalog"],
                                                                   "section": student["section"],
                                                                   "login_time": student["login_time"],
                                                                   "logout_time": student["logout_time"],
                                                                   "service": student["service"]})
        else:
            result = Database.DATABASE[LOGIN_HISTORY].insert_one({"eid": student["eid"], "barcode": student["barcode"],
                                                                  "first_name": student["first_name"],
                                                                  "last_name": student["last_name"],
                                                                  "subject": student["subject"],
                                                                  "catalog": student["catalog"],
                                                                  "section": student["section"],
                                                                  "login_time": student["login_time"],
                                                                  "logout_time": student["logout_time"],
                                                                  "service": student["service"]})

        if result.inserted_id is not None:
            return True
        return False

    # signs student out by removing their current visit document from the current_logins collection and moving that
    # document to the login_history collection
    # also used to manually sign out students without using input line on main page
    @staticmethod
    def sign_out(student_number, logout_time=""):
        if len(student_number) == 8:
            student_login = Database.DATABASE[CURRENT_LOGINS].find_one_and_delete({"eid": student_number})
        else:
            student_login = Database.DATABASE[CURRENT_LOGINS].find_one_and_delete({"barcode": student_number})

        if logout_time == "":
            student_login["logout_time"] = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        else:
            student_login["logout_time"] = logout_time
        result = Database.DATABASE[LOGIN_HISTORY].insert_one(student_login)
        if result.inserted_id is not None:
            return True
        return False

    ####################################################################################################################
    #                                              students page methods
    ####################################################################################################################

    # adds a student to database
    # returns true if student was added to system, returns false otherwise
    @staticmethod
    def add_student(eid, first_name, last_name, barcode="", email=""):
        found_doc = Database.DATABASE[STUDENTS].find_one({"eid": eid})
        if found_doc is None:
            enrolled_list = []
            Database.DATABASE[STUDENTS].insert_one({"eid": eid, "first_name": first_name, "last_name": last_name,
                                                    "barcode": barcode, "email": email,
                                                    "enrolled_list": enrolled_list})
            return True
        return False

    # returns list of all students
    @staticmethod
    def get_all_students():
        return Database.DATABASE[STUDENTS].find({}, {"_id": 0})

    # changes last name of student whose eid is an_eid
    # returns true if student"s last name is changed to new_last_name, returns false otherwise
    @staticmethod
    def update_student_last_name(an_eid, new_last_name):
        result = Database.DATABASE[STUDENTS].update_one({"eid": an_eid}, {"$set": {"last_name": new_last_name}})
        if result.modified_count > 0:
            return True
        return False

    # changes first name of student whose eid is an_eid
    # returns true if student"s first name is changed to new_first_name, returns false otherwise
    @staticmethod
    def update_student_first_name(an_eid, new_first_name):
        result = Database.DATABASE[STUDENTS].update_one({"eid": an_eid}, {"$set": {"first_name": new_first_name}})
        if result.modified_count > 0:
            return True
        return False

    # changes email of student whose eid is an_eid
    # returns true if student"s email is changed to new_email, returns false otherwise
    @staticmethod
    def update_student_email(an_eid, new_email):
        result = Database.DATABASE[STUDENTS].update_one({"eid": an_eid}, {"$set": {"email": new_email}})
        if result.modified_count > 0:
            return True
        return False

    # changes barcode of student whose eid is an_eid
    # returns true if student"s barcode is changed to new_barcode, returns false otherwise
    @staticmethod
    def update_student_barcode(an_eid, new_barcode):
        result = Database.DATABASE[STUDENTS].update_one({"eid": an_eid}, {"$set": {"barcode": new_barcode}})
        if result.modified_count > 0:
            return True
        return False

    # changes eid of student whose eid is an_eid
    # returns true if student"s eid is changed to new_eid, returns false otherwise
    @staticmethod
    def update_student_eid(an_eid, new_eid):
        result = Database.DATABASE[STUDENTS].update_one({"eid": an_eid}, {"$set": {"eid": new_eid}})
        if result.modified_count > 0:
            return True
        return False

    # removes student whose eid is an_eid from system
    # returns true if student was deleted and returns false otherwise
    @staticmethod
    def remove_student(an_eid):
        result = Database.DATABASE[STUDENTS].delete_one({"eid": an_eid})
        if result.deleted_count > 0:
            return True
        return False

    ####################################################################################################################
    #                                               classes page methods
    ####################################################################################################################

    # adds a class whose "subject" is subject, "catalog" is catalog, "section" is section and "professor" is professor
    # catalog defaults to "99999" and section defaults to "99" if neither is provided
    # professor defaults to an empty dictionary if no professor is provided
    # returns true if class was successfully added and returns false otherwise
    @staticmethod
    def add_class(subject, catalog="99999", section="99", professor={}):
        found_doc = Database.DATABASE[CLASSES].find_one({"subject": subject, "catalog": catalog, "section": section})
        if found_doc is None:
            class_roster = []
            Database.DATABASE[CLASSES].insert_one({"subject": subject, "catalog": catalog, "section": section,
                                                   "professor": professor, "class_roster": class_roster})
            return True
        return False

    # returns list of all classes in the system
    @staticmethod
    def get_all_classes():
        return Database.DATABASE[CLASSES].find({}, {"_id": 0})

    # changes the subject of the class whose subject, catalog, and section fields match the given parameters
    # the class's subject field will be set to new_subject
    # returns true if class's subject is changed to new_subject and returns false otherwise
    @staticmethod
    def update_class_subject(new_subject, subject, catalog, section):
        result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                       {"$set": {"subject": new_subject}})
        if result.modified_count > 0:
            return True
        return False

    # changes the catalog of the class whose subject, catalog, and section fields match the given parameters
    # the class's catalog field will be set to new_catalog
    # returns true if class's catalog is changed to new_catalog and returns false otherwise
    @staticmethod
    def update_class_catalog(new_catalog, subject, catalog, section):
        result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                       {"$set": {"catalog": new_catalog}})
        if result.modified_count > 0:
            return True
        return False

    # changes the section of the class whose subject, catalog, and section fields match the given parameters
    # the class's section field will be set to new_section
    # returns true if class's section is changed to new_section and returns false otherwise
    @staticmethod
    def update_class_section(new_section, subject, catalog, section):
        result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog, "section": section},
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
        result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog, "section": section},
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
        result = Database.DATABASE[CLASSES].delete_one({"subject": subject, "catalog": catalog, "section": section})
        if result.deleted_count > 0:
            return True
        return False

    ####################################################################################################################
    #                                             professors page methods
    ####################################################################################################################

    # adds professor to system
    # returns true if professor was added, returns false otherwise
    @staticmethod
    def add_professor(first_name, last_name, email=""):
        found_doc = Database.DATABASE[PROFESSORS].find_one({"first_name": first_name,
                                                            "last_name": last_name, "email": email})
        if found_doc is None:
            Database.DATABASE[PROFESSORS].insert_one({"first_name": first_name, "last_name": last_name, "email": email})
            return True
        return False

    # returns list of all professors in the system
    @staticmethod
    def get_all_professors():
        return Database.DATABASE[PROFESSORS].find({}, {"_id": 0})

    # returns true if professor's first_name was changed to new_first_name, returns false otherwise
    @staticmethod
    def update_professor_first_name(new_first_name, first_name, last_name, email=""):
        result = Database.DATABASE[PROFESSORS].update_one({"first_name": first_name, "last_name": last_name,
                                                           "email": email},
                                                          {"$set": {"first_name": new_first_name}})

        if result.modified_count > 0:
            return True
        return False

    # returns true if professor's last_name was changed to new_last_name, returns false otherwise
    @staticmethod
    def update_professor_last_name(new_last_name, first_name, last_name, email=""):
        result = Database.DATABASE[PROFESSORS].update_one({"first_name": first_name, "last_name": last_name,
                                                           "email": email},
                                                          {"$set": {"last_name": new_last_name}})

        if result.modified_count > 0:
            return True
        return False

    # returns true if professor's email was changed to new_email, returns false otherwise
    @staticmethod
    def update_professor_email(new_email, first_name, last_name, email=""):
        result = Database.DATABASE[PROFESSORS].update_one({"first_name": first_name, "last_name": last_name,
                                                           "email": email},
                                                          {"$set": {"email": new_email}})

        if result.modified_count > 0:
            return True
        return False

    # returns true if professor was removed from system, returns false otherwise
    @staticmethod
    def remove_professor(first_name, last_name, email=""):
        result = Database.DATABASE[PROFESSORS].delete_one({"first_name": first_name, "last_name": last_name,
                                                           "email": email})

        if result.deleted_count > 0:
            return True
        return False

    ####################################################################################################################
    #                                             register page methods
    ####################################################################################################################

    # returns a list of all classes and the students in them
    @staticmethod
    def get_classes_with_students():
        return Database.DATABASE[CLASSES].find({}, {"_id": 0, "professor": 0})

    # registers student for a class by adding student to a class's class_roster field
    # returns (true, true) if student with eid "student_eid" was registered to the class whose subject, catalog and
    # section are "subject", "catalog" and "section" respectively,
    # returns (false, false) if student was not registered and did not have their enrolled_list updated,
    # returns (true, false) if student was registered for class but their enrolled_list was not updated,
    # returns (false, true) if student was not registered but their enrolled_list was updated
    @staticmethod
    def register_student(student_eid, student_first_name, student_last_name, subject, catalog, section):
        # registers student by adding student info to class's class_roster field
        # result tells you whether or not the class's class_roster was updated
        result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog, "section": section},
                                                       {"$addToSet":
                                                            {"class_roster":
                                                                 {"student_eid": student_eid,
                                                                  "student_first_name": student_first_name,
                                                                  "student_last_name": student_last_name}}})

        # adds class info and registration info to student's enrolled_list field
        # student_result tells you whether or not the student's enrolled_list was updated
        student_result = Database.DATABASE[STUDENTS].update_one({"eid": student_eid,
                                                                 "enrolled_list":
                                                                     {"$not":
                                                                          {"$elemMatch":
                                                                               {"subject": subject,
                                                                                "catalog": catalog,
                                                                                "section": section}}}},
                                                                {"$push":
                                                                     {"enrolled_list":
                                                                          {"subject": subject,
                                                                           "catalog": catalog,
                                                                           "section": section,
                                                                           "registered_by": "meeeee",
                                                                           "registered_date":
                                                                               datetime.datetime.now().strftime(
                                                                                   "%m/%d/%Y %I:%M:%S %p")}}})

        if result.modified_count > 0 and student_result.modified_count > 0:
            return True, True
        elif result.modified_count > 0 and student_result.modified_count == 0:
            return True, False
        elif result.modified_count == 0 and student_result.modified_count > 0:
            return False, True
        return False, False

    # unregisters student from the class whose subject, catalog, and section are the given parameters subject, catalog,
    # and section respectively
    # returns true true if student was unregistered from the class and the class was removed from the student's
    # enrolled_list
    # returns true, false if student was unregistered from the class and the class was not removed from the student's
    # enrolled_list
    # returns false, true if student was not unregistered from the class and the class was removed from the student's
    # enrolled_list
    # returns false, false if student was not unregistered from the class and the class was not removed from the
    # student's enrolled_list
    @staticmethod
    def unregister_student(student_eid, student_first_name, student_last_name, subject, catalog, section):
        class_result = Database.DATABASE[CLASSES].update_one({"subject": subject, "catalog": catalog,
                                                              "section": section},
                                                             {"$pull": {"class_roster":
                                                                            {"student_eid": student_eid,
                                                                             "student_first_name": student_first_name,
                                                                             "student_last_name": student_last_name}}}
                                                             )

        student_result = Database.DATABASE[STUDENTS].update_one({"eid": student_eid},
                                                                {"$pull": {"enrolled_list":
                                                                               {"subject": subject,
                                                                                "catalog": catalog,
                                                                                "section": section}}})

        if class_result.modified_count > 0 and student_result.modified_count > 0:
            return True, True
        elif class_result.modified_count > 0 and student_result.modified_count == 0:
            return True, False
        elif class_result.modified_count == 0 and student_result.modified_count > 0:
            return False, True
        return False, False

    ####################################################################################################################
    #                                             login history page methods
    ####################################################################################################################

    # returns list of all logins
    @staticmethod
    def show_login_history():
        return Database.DATABASE[LOGIN_HISTORY].find({}, {"_id": 0})
