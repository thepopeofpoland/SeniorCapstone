import datetime as dt
import sqlalchemy as db

engine = db.create_engine('sqlite:///calendar.db')
connection = engine.connect()
metadata = db.MetaData()

family = db.Table('family', metadata, autoload_with=engine)
reservation = db.Table('reservation', metadata, autoload_with=engine)

metadata.create_all(engine)


# gets family information from the database
def retrieve_family_data():
    query = db.select(family.c.sirName, family.c.numMembers)
    result_temp = connection.execute(query)
    results = result_temp.fetchall()
    formatted_results = '\n'.join([str(row) for row in results])

    return formatted_results


def retrieve_cal_dates():
    query = db.select(reservation)
    result_temp = connection.execute(query)
    results = result_temp.fetchall()
    formatted_results = '\n'.join([f"({row[1].strftime('%m/%d/%Y')}, '{row[2]}')" for row in results])

    return formatted_results


def insert_family(famName, memNumber):
    test = db.insert(family).values(sirName=famName, numMembers=memNumber)

    try:
        # Execute the insert statement
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")

    except Exception as e:
        print("Error inserting data:", e)


def update_family(famName, memNumber):
    test = family.update().values(numMembers=memNumber).where(family.c.sirName==famName)

    try:
        # Execute the insert statement
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")

    except Exception as e:
        print("Error inserting data:", e)


def insert_reservation(date, name):
    # Attempt to parse the date string into a date object
    reserve = dt.datetime.strptime(date, '%m/%d/%Y').date()
    print(reserve)
    test = db.insert(reservation).values(reservation_date=reserve, family_name=name)

    try:
        # Execute the insert statement
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error inserting data:", e)


def remove_date(date, name):
    # figure out how to get the primary key from the selected date and delete by the primary key
    reserve = dt.datetime.strptime(date, '%m/%d/%Y').date()

    # Create a SQLAlchemy delete statement
    delete_entry = reservation.delete().where(
        (reservation.c.family_name == name) & (reservation.c.reservation_date == reserve)
    )
    # Execute the delete statement
    try:
        connection.execute(delete_entry)
        connection.commit()
        print("Reservation deleted successfully")

    except Exception as e:
        print("Error deleting reservation:", e)

# def conflict_check(date):
#     try:
#         conflicting_entries = []
#         reserve_date = dt.datetime.strptime(date, '%m/%d/%Y').date()
#
#         # Query the database to find entries that overlap with the given date range
#         query = reservation.select().where(
#                     )
#
#         result = connection.execute(query).fetchall()
#
#         # Iterate through the results and collect conflicting entries
#         for row in result:
#             conflicting_entries.append(row)
#
#         return conflicting_entries
#
#     except Exception as e:
#         print("Error checking for conflicting dates:", e)
#         return None