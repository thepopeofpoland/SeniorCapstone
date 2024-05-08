# import unittest
# from unittest.mock import MagicMock
# import sqlalchemy as db
# import dbconnect
# from dbconnect import retrieve_family_data, retrieve_cal_dates, insert_family, update_family, connection, family
#
#
# class TestDBConnect(unittest.TestCase):
#     def setUp(self):
#         self.mock_db = MagicMock()
#         self.mock_connection = MagicMock()
#         self.mock_execute = MagicMock()
#         self.mock_commit = MagicMock()
#         connection.execute = self.mock_execute
#         connection.commit = self.mock_commit
#
#     def test_retrieve_family_data(self):
#         mock_result = MagicMock()
#         mock_result.fetchall.return_value = [
#             ('Smith', 5),
#             ('Johnson', 3)
#         ]
#
#         connection.execute = MagicMock(return_value=mock_result)
#
#         result = retrieve_family_data()
#
#         expected_output = "('Smith', 5)\n('Johnson', 3)"
#
#         connection.execute.assert_called_once()
#
#         mock_result.fetchall.assert_called_once()
#
#         self.assertEqual(result, expected_output)
#
#     def test_retrieve_cal_dates(self,):
#         mock_result_temp = MagicMock()
#         mock_result_temp.fetchall.return_value = [
#             ('2024-04-12', 'Smith'),
#             ('2024-04-13', 'Doe')
#         ]
#
#         connection.execute = MagicMock(return_value=mock_result_temp)
#
#         result = retrieve_cal_dates()
#
#         expected_result = [('2024-04-12', 'Smith'), ('2024-04-13', 'Doe')]
#
#         connection.execute.assert_called_once()
#
#         mock_result_temp.fetchall.assert_called_once()
#
#         self.assertEqual(result, expected_result)
#
import unittest
from unittest.mock import MagicMock
import dbconnect  # assuming your code is in a module named my_module


class TestMyModule(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        dbconnect.db = self.mock_db

    def test_retrieve_family_data(self):
        # Prepare mock return value
        mock_result = [('Smith', 4), ('Johnson', 3)]
        mock_connection = MagicMock()
        mock_connection.execute.return_value.fetchall.return_value = mock_result
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.retrieve_family_data()

        # Assert the result
        self.assertEqual(result, mock_result)

    def test_retrieve_cal_dates(self):
        # Prepare mock return value
        mock_result = [('2024-01-01', 'Smith'), ('2024-02-01', 'Johnson')]
        mock_connection = MagicMock()
        mock_connection.execute.return_value.fetchall.return_value = mock_result
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.retrieve_cal_dates()

        # Assert the result
        self.assertEqual(result, mock_result)

    def test_insert_family(self):
        # Prepare mock return value
        mock_connection = MagicMock()
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.insert_family("Smith", 4)

        # Assert the result
        self.assertEqual(result, "")

    def test_update_family(self):
        # Prepare mock return value
        mock_connection = MagicMock()
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.update_family("Johnson", 5)

        # Assert the result
        self.assertEqual(result, "")

    def test_insert_reservation(self):
        # Prepare mock return value
        mock_connection = MagicMock()
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.insert_reservation("2024-01-01", "Smith")

        # Assert the result
        self.assertEqual(result, "")

    def test_remove_date(self):
        # Prepare mock return value
        mock_connection = MagicMock()
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.remove_date("2024-01-01", "Smith")

        # Assert the result
        self.assertEqual(result, "")

    def test_conflict_check(self):
        # Prepare mock return value
        mock_result = True
        mock_connection = MagicMock()
        mock_connection.execute.return_value.fetchone.return_value = mock_result
        self.mock_db.create_engine.return_value.connect.return_value = mock_connection

        # Call the function to test
        result = dbconnect.conflict_check("2024-01-01")

        # Assert the result
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
