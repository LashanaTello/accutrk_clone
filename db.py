from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
import datetime
from config import keys, defaultDB
from constants import STUDENTS, CLASSES, PROFESSORS, CURRENT_LOGINS, LOGIN_HISTORY, SEMESTER, SERVICES


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
    def get_current_logins():
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
            login_time = datetime.datetime.utcnow()

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
            student["login_time"] = datetime.datetime.utcnow()

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
            student_login["logout_time"] = datetime.datetime.utcnow()
        else:
            student_login["logout_time"] = logout_time
        result = Database.DATABASE[LOGIN_HISTORY].insert_one(student_login)
        if result.inserted_id is not None:
            return True, student_login["first_name"], student_login["last_name"]
        return False, student_login["first_name"], student_login["last_name"]

    # returns student eid, barcode, first_name and last_name that belongs to the student whose eid or barcode is
    # student_id
    @staticmethod
    def get_student_data(student_id):
        if len(student_id) == 8:
            student_info = Database.DATABASE[STUDENTS].find_one({"eid": student_id}, {"_id": 0, "eid": 1, "barcode": 1,
                                                                                      "first_name": 1, "last_name": 1})
        else:
            student_info = Database.DATABASE[STUDENTS].find_one({"barcode": student_id}, {"_id": 0, "eid": 1,
                                                                                          "barcode": 1, "first_name": 1,
                                                                                          "last_name": 1})

        return student_info

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
        return Database.DATABASE[STUDENTS].find({}, {"_id": 0}).sort([("last_name", ASCENDING),
                                                                      ("first_name", ASCENDING)])

    # returns list of classes that student with eid or barcode "student_id" is enrolled in
    @staticmethod
    def get_student_classes(student_id):
        if len(student_id) == 8:
            student_info = Database.DATABASE[STUDENTS].find_one({"eid": student_id}, {"_id": 0, "enrolled_list": 1})
        else:
            student_info = Database.DATABASE[STUDENTS].find_one({"barcode": student_id}, {"_id": 0, "enrolled_list": 1})

        return student_info

    # changes data of a_student to updated_student in database
    # returns true if change was successful, returns false otherwise
    @staticmethod
    def update_student(eid, updated_student):
        result = Database.DATABASE[STUDENTS].update_one({"eid": eid},
                                                        {"$set": {"eid": updated_student["eid"],
                                                                  "first_name": updated_student["first_name"],
                                                                  "last_name": updated_student["last_name"],
                                                                  "barcode": updated_student["barcode"],
                                                                  "email": updated_student["email"]}})
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

    @staticmethod
    def get_classes_with_size():
        command = [{"$project": {"_id": 0, "subject": 1, "catalog": 1, "section": 1, "professor": 1, "class_roster": 1,
                                 "count": {"$size": "$class_roster"}}}]
        return Database.DATABASE[CLASSES].aggregate(command)

    # returns list of all classes in the system
    @staticmethod
    def get_all_classes():
        return Database.DATABASE[CLASSES].find({}, {"_id": 0})

    # returns list of all classes in system with just the subject, catalog, section and professor
    @staticmethod
    def get_all_class_names():
        return Database.DATABASE[CLASSES].find({},
                                               {"_id": 0, "subject": 1, "catalog": 1, "section": 1, "professor": 1}) \
            .sort([("subject", ASCENDING), ("catalog", ASCENDING), ("section", ASCENDING)])

    # changes the data of old_class in database to new_class
    # returns true if old_class is changed and returns false otherwise
    @staticmethod
    def update_class(old_class, new_class):
        result = Database.DATABASE[CLASSES].update_one({"subject": old_class["subject"],
                                                        "catalog": old_class["catalog"],
                                                        "section": old_class["section"]},
                                                       {"$set": {"subject": new_class["subject"],
                                                                 "catalog": new_class["catalog"],
                                                                 "section": new_class["section"],
                                                                 "professor": new_class["professor"]}})
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

    # changes data of og_professor to updated_professor in database
    # returns true if change was successful, returns false otherwise
    @staticmethod
    def update_professor(og_professor, updated_professor):
        result = Database.DATABASE[PROFESSORS].update_one({"first_name": og_professor["first_name"],
                                                           "last_name": og_professor["last_name"],
                                                           "email": og_professor["email"]},
                                                          {"$set": {"first_name": updated_professor["first_name"],
                                                                    "last_name": updated_professor["last_name"],
                                                                    "email": updated_professor["email"]}})
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
    # section are "subject", "catalog" and "section" respectively
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

        # if nothing was modified, then the class you're trying to register the student for doesn't exist
        if result.modified_count == 0:
            return False

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
                                                                               datetime.datetime.utcnow()}}})

        if result.modified_count > 0 and student_result.modified_count > 0:
            return True, True
        return True, False  # student already registered for this class or student does not exist

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
    def get_login_history():
        return Database.DATABASE[LOGIN_HISTORY].find({}, {"_id": 0})

    # edits the entries in the login_history collection
    # returns true if original_login was successfully changed to edited_login, returns false otherwise
    @staticmethod
    def edit_login(original_login, edited_login):
        result = Database.DATABASE[LOGIN_HISTORY].update_one({"eid": original_login["eid"],
                                                              "barcode": original_login["barcode"],
                                                              "first_name": original_login["first_name"],
                                                              "last_name": original_login["last_name"],
                                                              "subject": original_login["subject"],
                                                              "catalog": original_login["catalog"],
                                                              "section": original_login["section"],
                                                              "login_time": original_login["login_time"],
                                                              "logout_time": original_login["logout_time"],
                                                              "service": original_login["service"]},
                                                             {"$set":
                                                                  {"eid": edited_login["eid"],
                                                                   "barcode": edited_login["barcode"],
                                                                   "first_name": edited_login["first_name"],
                                                                   "last_name": edited_login["last_name"],
                                                                   "subject": edited_login["subject"],
                                                                   "catalog": edited_login["catalog"],
                                                                   "section": edited_login["section"],
                                                                   "login_time": edited_login["login_time"],
                                                                   "logout_time": edited_login["logout_time"],
                                                                   "service": edited_login["service"]}
                                                              })

        if result.modified_count > 0:
            return True
        return False

    # removes a login entry from login_history collection
    # returns true if login_to_remove is removed, returns false otherwise
    @staticmethod
    def remove_login(login_to_remove):
        result = Database.DATABASE[LOGIN_HISTORY].delete_one({"eid": login_to_remove["eid"],
                                                              "barcode": login_to_remove["barcode"],
                                                              "first_name": login_to_remove["first_name"],
                                                              "last_name": login_to_remove["last_name"],
                                                              "subject": login_to_remove["subject"],
                                                              "catalog": login_to_remove["catalog"],
                                                              "section": login_to_remove["section"],
                                                              "login_time": login_to_remove["login_time"],
                                                              "logout_time": login_to_remove["logout_time"],
                                                              "service": login_to_remove["service"]})

        if result.deleted_count > 0:
            return True
        return False

    ####################################################################################################################
    #                                             semester page methods
    ####################################################################################################################

    # officially creates semester by adding semester_name, semester_start_date and semester_end_date to the
    # semester collection in a new database whose name is semester_name
    # returns true if that operation was successful, returns false if that operation was unsuccessful or if
    # semester_name is the same as a previous semester
    @staticmethod
    def create_semester(semester_name, semester_start_date, semester_end_date):
        if semester_name == "media" or semester_name == "local" or semester_name == "admin":
            return False

        client = MongoClient(Database.uri)
        db_names = client.list_database_names()

        # semester name must be unique
        for db_name in db_names:
            if db_name != "media" and db_name != "local" and db_name != "admin":
                a_db = client[db_name]
                semester = a_db[SEMESTER].find_one({}, {"_id": 0})
                if semester is not None and (db_name == semester_name or semester["semester_name"] == semester_name):
                    return False

        new_db = client[semester_name]
        result = new_db[SEMESTER].insert_one({"semester_name": semester_name,
                                              "semester_start_date": semester_start_date,
                                              "semester_end_date": semester_end_date})

        if result.inserted_id is not None:
            return True
        return False

    # returns list of all semesters with their start and end dates
    @staticmethod
    def get_all_semesters():
        client = MongoClient(Database.uri)
        db_names = client.list_database_names()
        semesters = []
        for db_name in db_names:
            if db_name != "media" and db_name != "local" and db_name != "admin":
                new_db = client[db_name]
                semesters.append(new_db[SEMESTER].find_one({}, {"_id": 0}))

        return semesters

    # sets the current active semester to the semester named semester_name and returns true
    @staticmethod
    def set_semester(semester_name):
        client = MongoClient(Database.uri)
        db_names = client.list_database_names()
        db_to_set = ""

        for db_name in db_names:
            if db_name != "media" and db_name != "local" and db_name != "admin":
                new_db = client[db_name]
                semester = new_db[SEMESTER].find_one({}, {"_id": 0})
                if semester is not None and semester_name == semester["semester_name"]:
                    db_to_set = db_name

        # set default database name
        f = open(defaultDB.dbNameFile, "w")
        f.write(db_to_set)
        f.close()

        return True

    # Edits any info about original_semester to match edited_semester and returns true if the change was
    # successfully updated in the database
    # returns true if that operation was successful, returns false otherwise
    @staticmethod
    def edit_semester(original_semester, edited_semester):
        client = MongoClient(Database.uri)
        db_names = client.list_database_names()
        for db_name in db_names:
            if db_name == original_semester["semester_name"]:
                a_db = client[db_name]
                result = a_db[SEMESTER].update_one({"semester_name": original_semester["semester_name"]},
                                                   {"$set":
                                                        {"semester_name": edited_semester["semester_name"],
                                                         "semester_start_date": edited_semester["semester_start_date"],
                                                         "semester_end_date": edited_semester["semester_end_date"]}})

                if result.modified_count > 0:
                    return True
        return False

    # returns name of semester
    @staticmethod
    def get_semester_name():
        return Database.DATABASE[SEMESTER].find_one({}, {"_id": 0})["semester_name"]

    ####################################################################################################################
    #                                             service page methods
    ####################################################################################################################

    # returns True if service was created and added to database, returns False otherwise
    @staticmethod
    def add_service(service):
        found_doc = Database.DATABASE[SERVICES].find_one({"service": service})
        if found_doc is None:
            Database.DATABASE[SERVICES].insert_one({"service": service})
            return True
        return False

    # returns list of all services
    @staticmethod
    def get_all_services():
        return Database.DATABASE[SERVICES].find({}, {"_id": 0})

    # returns True if service is changed to new_service, returns False otherwise
    @staticmethod
    def edit_service(service, new_service):
        result = Database.DATABASE[SERVICES].update_one({"service": service}, {"$set": {"service": new_service}})

        if result.modified_count > 0:
            return True
        return False

    # returns True if service was deleted from database, returns False otherwise
    @staticmethod
    def remove_service(service):
        result = Database.DATABASE[SERVICES].delete_one({"service": service})

        if result.deleted_count > 0:
            return True
        return False
