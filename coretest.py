import unittest
from unittest.mock import patch, MagicMock
import core
import dbconnect


class TestCalendarApp(unittest.TestCase):
    def setUp(self):
        # Replace the functions with mocks
        dbconnect.retrieve_family_data = MagicMock()
        dbconnect.retrieve_cal_dates = MagicMock()
        dbconnect.insert_family = MagicMock()
        dbconnect.update_family = MagicMock()

    def test_list_data_returns_correct_data(self):
        expected_family_data = [{'name': 'Smith', 'age': 32}, {'name': 'Doe', 'age': 28}]
        dbconnect.retrieve_family_data.return_value = expected_family_data

        # Call the function
        result = core.list_data()

        # Check the result
        self.assertEqual(result, expected_family_data)

    def test_list_cal_dates_returns_correct_data(self):
        expected_calendar_dates = [{'date': '2024-04-12', 'event': 'Meeting'},
                                   {'date': '2024-04-13', 'event': 'Workshop'}]
        dbconnect.retrieve_cal_dates.return_value = expected_calendar_dates

        # Call the function
        result = core.list_cal_dates()

        # Check the result
        self.assertEqual(result, expected_calendar_dates)

    def test_add_family(self):
        name = "Smith"
        family_members = 5
        result = core.add_family(name, family_members)

        dbconnect.insert_family.assert_called_once_with(name, family_members)
        self.assertEqual(result, "")

        dbconnect.insert_family.reset_mock()

        result = core.add_family('Smith123', family_members)

        dbconnect.insert_family.assert_not_called()
        self.assertEqual(result, "Not a valid family name or number of members.")

    def test_update_family(self):
        name = "Smith"
        family_members = 4
        result = core.update_family(family_members, name)

        dbconnect.update_family.assert_called_once_with(name, family_members)
        self.assertEqual(result, "")

        dbconnect.update_family.reset_mock()
        result = core.update_family(family_members, 'Smith123')

        dbconnect.update_family.assert_not_called()
        self.assertEqual(result, "Not a valid family name or number of members.")