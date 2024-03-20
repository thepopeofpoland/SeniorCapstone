import dbconnect


def list_data():
    """
    This function will return a list of all the data in the family table of the database
    :return:
    """
    return dbconnect.retrieve_family_data()


def list_cal_dates():
    """
    This function will return a list of all the data in the reservation table of the database
    :return:
    """
    return dbconnect.retrieve_cal_dates()


def add_date():
    pass
    # save date as sqlite date type text and look at the python calendar module.


def add_family(surname, family_members):
    """
              Creates a new entry to the family table of the DB.
              :param surname: Name of the new entry to the family table.
              :type surname: String
              :param family_members: Provide the new updated number of people in that family.
              :type family_members: Integer
              """
    dbconnect.insert_family(surname, family_members)


def add_reservation(date, name):
    """
                  Creates a new entry to the family table of the DB.
                  :param date: Brings in a string representing the date of the reservation.
                  :type date: String
                  :param name: Name that is creating the reservation.
                  :type name: String
                  """
    dbconnect.insert_reservation(date, name)


# #def update_family(family_members):
#     """
#            Modifies an entry to the family Data
#
#            :param family_members: provide the new updated number of people in that family
#            :type family_members: integer
#            """
#
#      need to add this still


def remove_date(date, name):
    dbconnect.remove_date(date, name)


# def conflict_check(date):
#     return dbconnect.conflict_check(date)
