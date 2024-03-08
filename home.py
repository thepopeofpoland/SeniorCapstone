import json
import DBConnect


def list_data():
    """
    This function will return a list of all the data in the family table of the database
    :return:
    """
    return DBConnect.retrieve_family_data()


def list_cal_dates():
    """
    This function will return a list of all the data in the reservation table of the database
    :return:
    """
    return DBConnect.retrieve_cal_dates()


def add_date():
    pass
    # save date as sqlite date type text and look at the python calendar module.


def add_family(sir_name, family_members):
    """
              Creates a new entry to the family table of the DB.
              :param sir_name: Name of the new entry to the family table.
              :type sir_name: String
              :param family_members: Provide the new updated number of people in that family.
              :type family_members: Integer
              """
    DBConnect.insert_family(sir_name, family_members)


def add_reservation(date, name):
    """
                  Creates a new entry to the family table of the DB.
                  :param date: Brings in a string representing the date of the reservation.
                  :type date: String
                  :param name: Name that is creating the reservation.
                  :type name: String
                  """
    DBConnect.insert_reservation(date, name)


def update_family(family_members):
    """
           Modifies an entry to the family Data

           :param family_members: provide the new updated number of people in that family
           :type family_members: integer
           """

    # need to add this still


def remove_date(date, name):
    DBConnect.remove_date(date, name)


def conflict_check(date):
    return DBConnect.conflict_check(date)

