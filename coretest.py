import unittest
from unittest.mock import MagicMock
import core
import dbconnect


class TestCalendarApp(unittest.TestCase):
    def setUp(self):
        # Replace the functions with mocks
        dbconnect.retrieve_family_data = MagicMock()
        dbconnect.retrieve_cal_dates = MagicMock()
        dbconnect.insert_family = MagicMock()
        dbconnect.update_family = MagicMock()
        dbconnect.remove_date = MagicMock()

# list data test
    def test_list_data_returns_correct_data(self):
        expected_family_data = [{'name': 'Smith', 'family_num': 3}, {'name': 'Doe', 'family_num': 2}]
        dbconnect.retrieve_family_data.return_value = expected_family_data

        result = core.list_data()

        self.assertEqual(result, expected_family_data)

# list cal data test
    def test_list_cal_dates_returns_correct_data(self):
        expected_calendar_dates = [{'date': '2024-04-12', 'surname': 'Smith'},
                                   {'date': '2024-04-13', 'surname': 'Pope'}]
        dbconnect.retrieve_cal_dates.return_value = expected_calendar_dates

        result = core.list_cal_dates()

        self.assertEqual(result, expected_calendar_dates)

# add family tests
    def test_add_family_valid_input(self):
        surname = "Smith"
        family_members = 5
        dbconnect.insert_family.return_value = "Family added"

        result = core.add_family(surname, family_members)

        dbconnect.insert_family.assert_called_once_with(surname, family_members)
        self.assertEqual(result, "Family added")

    def test_add_family_invalid_surname(self):
        surname = "Smith123"
        family_members = 4

        result = core.add_family(surname, family_members)

        self.assertEqual(result, "Not a valid family name or number of members.")
        dbconnect.insert_family.assert_not_called()

    def test_add_family_invalid_family_members(self):
        surname = "Johnson"
        family_members = "three"

        with self.assertRaises(ValueError):
            core.add_family(surname, family_members)

        dbconnect.insert_family.assert_not_called()

# update family tests
    def test_update_family_valid_input(self):
        name = "Smith"
        family_members = 4
        dbconnect.update_family.return_value = "Family updated"

        result = core.update_family(family_members, name)

        dbconnect.update_family.assert_called_once_with(name, family_members)
        self.assertEqual(result, "Family updated")

    def test_update_family_invalid_name(self):
        name = "Smith123"
        family_members = 5

        result = core.update_family(family_members, name)

        self.assertEqual(result, "Not a valid family name or number of members.")
        dbconnect.update_family.assert_not_called()

    def test_update_family_invalid_family_members(self):
        name = "Smith"
        family_members = "five"
        with self.assertRaises(ValueError):
            core.update_family(family_members, name)

        dbconnect.update_family.assert_not_called()

# add reservation tests
    def test_add_reservation_valid_input(self):
        dbconnect.insert_reservation = MagicMock(return_value="Reservation added")

        date = "2023-04-10"
        name = "John"
        result = core.add_reservation(date, name)

        dbconnect.insert_reservation.assert_called_once_with(date, name)
        self.assertEqual(result, "Reservation added")

    def test_add_reservation_invalid_date(self):
        date = "2023/04/10"
        name = "John"
        result = core.add_reservation(date, name)

        self.assertEqual(result, "Not a valid reservation date or name.")

    def test_add_reservation_invalid_name(self):
        date = "2023-04-10"
        name = "John123"
        result = core.add_reservation(date, name)
        self.assertEqual(result, "Not a valid reservation date or name.")

# remove date tests
    def test_remove_date_valid_input(self):
        date = "2023-04-12"
        name = "Smith"
        dbconnect.remove_date.return_value = "Reservation removed"

        result = core.remove_date(date, name)

        dbconnect.remove_date.assert_called_once_with(date, name)
        self.assertEqual(result, "Reservation removed")

    def test_remove_date_invalid_date_format(self):
        date = "12-04-2023"
        name = "Smith"

        result = core.remove_date(date, name)

        self.assertEqual(result, "Not a valid reservation date or name.")
        dbconnect.remove_date.assert_not_called()

    def test_remove_date_invalid_name(self):
        date = "2023-04-12"
        name = "Smith123"

        result = core.remove_date(date, name)

        self.assertEqual(result, "Not a valid reservation date or name.")
        dbconnect.remove_date.assert_not_called()