import sqlalchemy as db

engine = db.create_engine('sqlite:///calendar.db')
connection = engine.connect()
metadata = db.MetaData()

family = db.Table('family', metadata, autoload_with=engine)
reservation = db.Table('reservation', metadata, autoload_with=engine)

metadata.create_all(engine)


def retrieve_family_data():
    query = db.select(family.c.surname, family.c.number_members)
    result_temp = connection.execute(query)
    results = result_temp.fetchall()
    formatted_results = '\n'.join([str(row) for row in results])

    return formatted_results


def retrieve_cal_dates():
    query = db.select(reservation.c.date, family.c.surname).join_from(reservation, family)
    result_temp = connection.execute(query)
    results = result_temp.fetchall()
    formatted_results = [(str(date), str(surname)) for date, surname in results]
    return formatted_results


def insert_family(fam_name, mem_number):
    test = db.insert(family).values(surname=fam_name, number_members=mem_number)

    try:
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")
        return ""

    except Exception as e:
        print("Error inserting data:", e)


def update_family(fam_name, mem_number):
    family_id_query = db.select(family.c.family_id).where(family.c.surname == fam_name)
    family_id_result = connection.execute(family_id_query)
    family_id = family_id_result.scalar()
    test = family.update().values(number_members=mem_number).where(family.c.family_id == family_id)

    try:
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")
        return ""

    except Exception as e:
        print("Error inserting data:", e)


def insert_reservation(date, name):
    family_id_query = db.select(family.c.family_id).where(family.c.surname == name)
    family_id_result = connection.execute(family_id_query)
    family_id = family_id_result.scalar()

    test = db.insert(reservation).values(date=date, family_id=family_id)

    try:
        connection.execute(test)
        connection.commit()
        print("Data inserted successfully")
        return ""

    except Exception as e:
        print("Error inserting data:", e)


def remove_date(date, name):
    family_id_query = db.select(family.c.family_id).where(family.c.surname == name)
    family_id_result = connection.execute(family_id_query)
    family_id = family_id_result.scalar()

    delete_entry = reservation.delete().where(
        (reservation.c.family_id == family_id) & (reservation.c.date == date)
    )
    try:
        connection.execute(delete_entry)
        connection.commit()
        print("Reservation deleted successfully")
        return ""

    except Exception as e:
        print("Error deleting reservation:", e)


def conflict_check(date):
    query = db.select(reservation.c.date).where(reservation.c.date == date)
    query_result = connection.execute(query)
    result = query_result.fetchone()

    return result is not None


def find_conflicts(date):
    query = db.select(reservation.c.date, family.c.surname).where(reservation.c.date == date).join_from(reservation, family)
    query_result = connection.execute(query)
    result = query_result.fetchall()

    return result
