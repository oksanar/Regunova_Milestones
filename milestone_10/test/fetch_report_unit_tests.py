import json
from unittest import main, TestCase
from unittest.mock import Mock, patch
from milestone_10.fetch_report import get_report
from milestone_10.test.server_unit_tests import ServerUnitTests


class FetchReportUnitTests(TestCase):
    test_data_report = """Report for HR department for April fetched.
Total 12, Anniversaries: 2
Employees:
- Apr 25 (36), Craig Morales
- Apr 5 (58), Madison Bennett MD
- Apr 24 (59), Krystal Gay
- Apr 15 (60), David Harper (is anniversary)
- Apr 14 (30), Tracy Mills (is anniversary)
- Apr 3 (39), Erik Faulkner
- Apr 28 (55), James Perry
- Apr 29 (35), Jason Gonzales
- Apr 2 (55), Joseph Berry
- Apr 1 (46), Todd Hull
- Apr 18 (34), Catherine Love
- Apr 9 (65), Jonathan Mccormick
"""

    @staticmethod
    def __get_birthdays_mock():
        response_mock = Mock()
        response_mock.return_value = \
            json.loads(ServerUnitTests.test_data_for_get_employees_birthdays)
        return response_mock

    @staticmethod
    def __get_anniversaries_mock():
        response_mock = Mock()
        response_mock.return_value = \
            json.loads(
                ServerUnitTests.test_data_for_get_employees_anniversaries)
        return response_mock

    @patch('milestone_10.fetch_report.get_anniversaries',
           new_callable=__get_anniversaries_mock)
    @patch('milestone_10.fetch_report.get_birthdays',
           new_callable=__get_birthdays_mock)
    def test_get_report(self, get_birthdays, get_anniversaries):
        self.assertEqual(get_report(department='HR', month_name='april'),
                         self.test_data_report)


if __name__ == '__main__':
    main(argv=[''], exit=False)
