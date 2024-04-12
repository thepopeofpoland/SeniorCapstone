import unittest
from unittest.mock import MagicMock
from dbconnect import retrieve_family_data, connection, family


class TestRetrieveFamilyData(unittest.TestCase):
    def test_retrieve_family_data(self):
        # Create a MagicMock for the result of the execute method
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
