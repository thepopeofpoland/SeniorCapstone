import dbconnect
import re


def list_data():
    """
    This function will return a list of all the data in the family table of the database

    """
    return dbconnect.retrieve_family_data()


def list_cal_dates():
    """
    This function will return a list of all the data in the reservation table of the database

    """
    return dbconnect.retrieve_cal_dates()


def add_family(surname, family_members):
    """
              Creates a new entry to the family table of the DB.
              :param surname: Name of the new entry to the family table.
              :type surname: String
              :param family_members: Provide the new updated number of people in that family.
              :type family_members: Integer
              """
    family_member = int(family_members)
    if not re.match(r'^[A-Za-z]+$', surname) or not isinstance(family_member, int):
        return "Not a valid family name or number of members."
    else:
        return dbconnect.insert_family(surname, family_members)


def update_family(family_members, name):
    """
           Modifies an entry to the family Data

           :param family_members: provide the new updated number of people in that family
           :type family_members: integer
           :param name: Name of the family to be updated
           :type name: String
           """
    family_member = int(family_members)
    if not re.match(r'^[A-Za-z]+$', name) or not isinstance(family_member, int):
        return "Not a valid family name or number of members."
    else:
        return dbconnect.update_family(name, family_members)


def add_reservation(date, name):
    """
                  Creates a new entry to the family table of the DB.
                  :param date: Brings in a string representing the date of the reservation.
                  :type date: String
                  :param name: Name that is creating the reservation.
                  :type name: String
                  """

    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date) or not re.match(r'^[A-Za-z]+$', name):
        return "Not a valid reservation date or name."
    else:
        return dbconnect.insert_reservation(date, name)



def remove_date(date, name):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date) or not re.match(r'^[A-Za-z]+$', name):
        return "Not a valid reservation date or name."
    else:
        return dbconnect.remove_date(date, name)


def conflict_check(date):
    return dbconnect.conflict_check(date)


def find_conflicts(date):
    return dbconnect.find_conflicts(date)