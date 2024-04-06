from typing import Dict
from flask import Flask, request, Response
from datetime import datetime
import csv
from dateutil.relativedelta import relativedelta
import calendar
import json


def generate_months():
    months = []
    for m in range(1, 12):
        curr = datetime(2024, m, 1)
        month = curr.strftime("%B")
        months.append(str(month).lower())
    return months


MONTHS = generate_months()


def get_splitted_date(string_date: str) -> Dict:
    date_time_parts = str(string_date).split('-')
    return {
        'year': int(date_time_parts[0]),
        'month': int(date_time_parts[1]),
        'day': int(date_time_parts[2])
    }


def filter_by_params(month: str,
                     department: str,
                     item: dict,
                     by_field_name='date_of_birth'):
    date_time_parts = get_splitted_date(item[by_field_name])
    if date_time_parts['month'] == (MONTHS.index(month) + 1) \
       and item['department'] == department:
        return item
    return None


def get_age(date_of_birth, current_date) -> int:
    dob = get_splitted_date(date_of_birth)
    num_of_days_in_month = calendar.monthrange(dob['year'], dob['month'])[1]
    dt1 = datetime(current_date.year, dob['month'], num_of_days_in_month)
    dt2 = datetime(dob['year'], dob['month'], dob['day'])
    age = relativedelta(dt1, dt2).years
    return age


def is_anniversary(age: int) -> bool:
    return age % 10 == 0 or age % 25 == 0


def format_date(date: str):
    date_parts = get_splitted_date(date)
    date_date = datetime(date_parts['year'],
                         date_parts['month'],
                         date_parts['day'])
    return date_date.strftime('%b %d').replace('0', '')


def get_employees_birthdays_by_department(filename: str,
                                          month_name: str,
                                          department: str):
    filtered_data = {'total': 0, 'employees': []}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        current_date = datetime.now()
        for item in reader:
            filtered_item = filter_by_params(month_name, department, item)
            if filtered_item is not None:
                filtered_data['total'] += 1
                age = get_age(item['date_of_birth'], current_date)
                user_data = {'id': item['id'],
                             'name': item['name'],
                             'birthday': format_date(item['date_of_birth']),
                             'age': age}
                filtered_data['employees'].append(user_data)

    return filtered_data


def get_employees_anniversaries_by_department(filename: str,
                                              month_name: str,
                                              department: str):
    filtered_data = {'total': 0, 'employees': []}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        current_date = datetime.now()
        for item in reader:
            filtered_item = filter_by_params(month_name, department, item)
            if filtered_item:
                age = get_age(item['date_of_birth'], current_date)
                if is_anniversary(age):
                    filtered_data['total'] += 1
                    birthday = format_date(item['date_of_birth'])
                    user_data = {'id': item['id'],
                                 'name': item['name'],
                                 'birthday': birthday,
                                 'age': age}
                    filtered_data['employees'].append(user_data)
        return filtered_data


app = Flask(__name__)

'''GET /birthdays?month=april&department=HR'''


@app.get('/birthdays')
def getBirthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    print(department)
    result = get_employees_birthdays_by_department('database.csv',
                                                   month,
                                                   department)
    return Response(response=json.dumps(result),
                    status=200,
                    mimetype="application/json")


'''GET /anniversaries?month=april&department=HR'''


@app.get('/anniversaries')
def getAnniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    print(department)
    result = get_employees_anniversaries_by_department('database.csv',
                                                       month,
                                                       department)
    return Response(response=json.dumps(result),
                    status=200,
                    mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=False, port=8001)
