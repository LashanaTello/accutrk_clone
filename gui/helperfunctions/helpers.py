import pytz


# converts utc_time to US/Eastern time and returns it in string format
def convert_time(utc_time):
    localized = pytz.utc.localize(utc_time, is_dst=None).astimezone(pytz.timezone("US/Eastern"))
    return localized.strftime("%m/%d/%Y %I:%M:%S %p")


# combines subject, catalog, and section into one string with a dash before the section
def combine_into_class(subject, catalog, section):
    return subject + " " + catalog + " - " + section
