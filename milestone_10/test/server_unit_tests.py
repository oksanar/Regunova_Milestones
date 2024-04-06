import csv
import json
from unittest import main, TestCase
from datetime import datetime
from milestone_10.server import filter_by_params, \
                                format_date, \
                                get_age, \
                                get_employees_anniversaries_by_department, \
                                get_employees_birthdays_by_department, \
                                get_splitted_date, \
                                is_anniversary


class ServerUnitTests(TestCase):
    input_test_file_content = []
    input_test_file = 'database.csv'
    test_birthdate = '1990-12-15'
    test_birthdate_splitted = {'year': 1990,
                               'month': 12,
                               'day': 15}
    test_data_for_get_employees_birthdays = """{
 "total": 12,
 "employees": [
  {
   "id": "66",
   "name": "Craig Morales",
   "birthday": "Apr 25",
   "age": 36
  },
  {
   "id": "107",
   "name": "Madison Bennett MD",
   "birthday": "Apr 5",
   "age": 58
  },
  {
   "id": "143",
   "name": "Krystal Gay",
   "birthday": "Apr 24",
   "age": 59
  },
  {
   "id": "187",
   "name": "David Harper",
   "birthday": "Apr 15",
   "age": 60
  },
  {
   "id": "284",
   "name": "Tracy Mills",
   "birthday": "Apr 14",
   "age": 30
  },
  {
   "id": "296",
   "name": "Erik Faulkner",
   "birthday": "Apr 3",
   "age": 39
  },
  {
   "id": "304",
   "name": "James Perry",
   "birthday": "Apr 28",
   "age": 55
  },
  {
   "id": "311",
   "name": "Jason Gonzales",
   "birthday": "Apr 29",
   "age": 35
  },
  {
   "id": "379",
   "name": "Joseph Berry",
   "birthday": "Apr 2",
   "age": 55
  },
  {
   "id": "438",
   "name": "Todd Hull",
   "birthday": "Apr 1",
   "age": 46
  },
  {
   "id": "505",
   "name": "Catherine Love",
   "birthday": "Apr 18",
   "age": 34
  },
  {
   "id": "522",
   "name": "Jonathan Mccormick",
   "birthday": "Apr 9",
   "age": 65
  }
 ]
}"""
    test_data_for_get_employees_anniversaries = """{
 "total": 2,
 "employees": [
  {
   "id": "187",
   "name": "David Harper",
   "birthday": "Apr 15",
   "age": 60
  },
  {
   "id": "284",
   "name": "Tracy Mills",
   "birthday": "Apr 14",
   "age": 30
  }
 ]
}"""

    def setUp(self):
        with open(self.input_test_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.input_test_file_content.append(row)

    def test_get_splitted_date(self):
        self.assertDictEqual(get_splitted_date(
            string_date=self.test_birthdate),
            self.test_birthdate_splitted)

    def test_filter_by_params(self):
        is_not_none_case_input_data = {'month': 'april',
                                       'department': 'HR',
                                       'item': self.input_test_file_content[65]
                                       }
        is_none_case_input_data = {'month': 'april',
                                   'department': 'HR',
                                   'item': self.input_test_file_content[66]
                                   }

        self.assertDictEqual(d1=filter_by_params(
            month=is_not_none_case_input_data['month'],
            department=is_not_none_case_input_data['department'],
            item=is_not_none_case_input_data['item']),
            d2=self.input_test_file_content[65])
        self.assertIsNone(filter_by_params(
            month=is_none_case_input_data['month'],
            department=is_none_case_input_data['department'],
            item=is_none_case_input_data['item']))

    def test_get_age(self):
        self.assertEqual(get_age(date_of_birth=self.test_birthdate,
                                 current_date=datetime(year=2024,
                                                       month=12,
                                                       day=15)), 34)

    def test_is_anniversary(self):
        self.assertTrue(is_anniversary(50))
        self.assertTrue(is_anniversary(25))
        self.assertFalse(is_anniversary(46))

    def test_format_date(self):
        self.assertEqual(format_date(self.test_birthdate), 'Dec 15')
        self.assertEqual(format_date('2000-04-05'), 'Apr 5')

    def test_get_employees_birthdays_by_department(self):
        function_result = get_employees_birthdays_by_department(
            filename='database.csv',
            month_name='april',
            department='HR')
        self.assertEqual(
            json.dumps(function_result, indent=1),
            self.test_data_for_get_employees_birthdays)

    def test_get_employees_anniversaries_by_department(self):
        function_result = get_employees_anniversaries_by_department(
            filename='database.csv',
            month_name='april',
            department='HR')
        self.assertEqual(
            json.dumps(function_result, indent=1),
            self.test_data_for_get_employees_anniversaries)


if __name__ == '__main__':
    main(argv=[''], exit=False)
