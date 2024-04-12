import unittest
from unittest.mock import MagicMock
import sqlalchemy as db
import dbconnect
from dbconnect import retrieve_family_data, retrieve_cal_dates, insert_family, update_family, connection, family


class TestDBConnect(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_connection = MagicMock()
        self.mock_execute = MagicMock()
        self.mock_commit = MagicMock()
        connection.execute = self.mock_execute
        connection.commit = self.mock_commit

    def test_retrieve_family_data(self):
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            ('Smith', 5),
            ('Johnson', 3)
        ]

        connection.execute = MagicMock(return_value=mock_result)

        result = retrieve_family_data()

        expected_output = "('Smith', 5)\n('Johnson', 3)"

        connection.execute.assert_called_once()

        mock_result.fetchall.assert_called_once()

        self.assertEqual(result, expected_output)

    def test_retrieve_cal_dates(self,):
        mock_result_temp = MagicMock()
        mock_result_temp.fetchall.return_value = [
            ('2024-04-12', 'Smith'),
            ('2024-04-13', 'Doe')
        ]

        connection.execute = MagicMock(return_value=mock_result_temp)

        result = retrieve_cal_dates()

        expected_result = [('2024-04-12', 'Smith'), ('2024-04-13', 'Doe')]

        connection.execute.assert_called_once()

        mock_result_temp.fetchall.assert_called_once()

        self.assertEqual(result, expected_result)

