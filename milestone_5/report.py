import sys
from datetime import datetime
import csv
from dateutil.relativedelta import relativedelta
import calendar


def generate_months():
    months = []
    for m in range(1, 12):
        curr = datetime(2024, m, 1)
        month = curr.strftime("%B")
        months.append(str(month).lower())
    return months


MONTHS = generate_months()


def get_splitted_date(string_date: str):
    date_time_parts = str(string_date).split('-')
    return {
        'year': int(date_time_parts[0]),
        'month': int(date_time_parts[1]),
        'day': int(date_time_parts[2])
    }


def filter_by_month(month: str, item: dict, by_field_name='date_of_birth'):
    date_time_parts = get_splitted_date(item[by_field_name])
    if date_time_parts['month'] == (MONTHS.index(month) + 1):
        return item
    return None


def is_anniversary(date_of_birth, current_date):
    dob = get_splitted_date(date_of_birth)
    num_of_days_in_month = calendar.monthrange(dob['year'], dob['month'])[1]
    dt1 = datetime(current_date.year, dob['month'], num_of_days_in_month)
    dt2 = datetime(dob['year'], dob['month'], dob['day'])
    age = relativedelta(dt1, dt2)
    return age.years % 10 == 0 or age.years % 25 == 0


def prepare_report_data(filename, month_name, is_verbose=False):
    filtered_data = {
        'birthdays': {'total': 0, 'by_departments': dict()},
        'anniversaries': {'total': 0, 'by_departments': dict()}
    }
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        current_date = datetime.now()
        for item in reader:
            filtered_item = filter_by_month(month_name, item)
            if filtered_item:
                filtered_data['birthdays']['total'] += 1
                has_department = filtered_data['birthdays']['by_departments'].get(filtered_item['department'])
                if has_department is None:
                    filtered_data['birthdays']['by_departments'][filtered_item['department']] = {'total': 1, 'names': []}
                else:
                    filtered_data['birthdays']['by_departments'][filtered_item['department']]['total'] += 1
                if is_verbose:
                    filtered_data['birthdays']['by_departments'][filtered_item['department']]['names'].append(item['name'])
                if is_anniversary(item['date_of_birth'], current_date):
                    filtered_data['anniversaries']['total'] += 1
                    has_department = filtered_data['anniversaries']['by_departments'].get(filtered_item['department'])
                    if has_department is None:
                        filtered_data['anniversaries']['by_departments'][filtered_item['department']] = {'total': 1, 'names': []}
                    else:
                        filtered_data['anniversaries']['by_departments'][filtered_item['department']]['total'] += 1
                    if is_verbose:
                        filtered_data['anniversaries']['by_departments'][filtered_item['department']]['names'].append(item['name'])
    return filtered_data


def print_report(report_data: dict, month_name: str, is_verbose=False):
    result = f'Report for {month_name.capitalize()} generated:\n'
    result += '--- Birthdays ---\n'
    result += f"Total: {report_data['birthdays']['total']}\n"
    result += 'By department:\n'
    by_departments = report_data['birthdays']['by_departments'].keys()
    for department in by_departments:
        result += f" - {department}: {report_data['birthdays']['by_departments'][department]['total']}\n"
        if is_verbose:
            for name in report_data['birthdays']['by_departments'][department]['names']:
                result += f"   - {name}\n"
    result += '--- Anniversaries ---\n'
    result += f"Total: {report_data['anniversaries']['total']}\n"
    result += 'By department:\n'
    by_departments = report_data['anniversaries']['by_departments'].keys()
    for department in by_departments:
        result += f" - {department}: {report_data['anniversaries']['by_departments'][department]['total']}\n"
        if is_verbose:
            for name in report_data['anniversaries']['by_departments'][department]['names']:
                result += f"   - {name}\n"
    return result


if __name__ == '__main__':
    arg = sys.argv[1:]
    arg_len = len(arg)
    if arg_len < 2:
        raise ValueError('''Please provide database filename and month name.
As Example:
# Without verbose:
python3 report.py database.csv april
# With verbose:
python3 report.py database.csv april -v
        ''')
    filename = arg[0]
    month_name = arg[1]
    is_verbose = False
    if arg_len >= 3:
        is_verbose = arg[2] == '-v'

    report_data = prepare_report_data(filename, month_name, is_verbose)
    print(print_report(report_data, month_name, is_verbose))